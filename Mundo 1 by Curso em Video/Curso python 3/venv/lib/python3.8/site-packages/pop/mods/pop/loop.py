# -*- coding: utf-8 -*-
"""
The main interface for management of the aio loop
"""
# Import python libs
import asyncio
import os
import pop.hub
import signal
import functools
from typing import Callable, Iterable, Generator

__virtualname__ = "loop"


def __virtual__(hub: "pop.hub.Hub"):
    return True


def create(hub: "pop.hub.Hub"):
    """
    Create the loop at hub.pop.Loop
    """
    if not hasattr(hub.pop, "Loop"):
        hub.pop.loop.FUT_QUE = asyncio.Queue()
        if os.name == "nt":
            hub.pop.Loop = asyncio._get_running_loop()
            if hub.pop.Loop is not None:
                return
            # The default event loop on Windows, "SelectorEventLoop" has certain limitations
            # ProactorEventLoop makes use of Window's I/O Completion Ports:
            #   https://docs.microsoft.com/en-ca/windows/win32/fileio/i-o-completion-ports
            hub.pop.Loop = asyncio.ProactorEventLoop()
            asyncio.set_event_loop(hub.pop.Loop)
        else:
            hub.pop.Loop = asyncio.get_event_loop()


def call_soon(hub: "pop.hub.Hub", ref: str, *args, **kwargs):
    """
    Schedule a coroutine to be called when the loop has time. This needs
    to be called after the creation fo the loop
    """
    fun = hub.pop.ref.get_func(ref)
    hub.pop.Loop.call_soon(functools.partial(fun, *args, **kwargs))


def ensure_future(hub: "pop.hub.Hub", ref: str, *args, **kwargs):
    """
    Schedule a coroutine to be called when the loop has time. This needs
    to be called after the creation fo the loop. This function also uses
    the hold system to await the future when it is done making it easy
    to create a future that will be cleanly awaited in the background.
    """
    fun = getattr(hub, ref)
    future = asyncio.ensure_future(fun(*args, **kwargs))

    def callback(fut):
        hub.pop.loop.FUT_QUE.put_nowait(fut)

    future.add_done_callback(callback)
    return future


def start(
    hub: "pop.hub.Hub",
    *coros,
    hold: bool = False,
    sigint: Callable = None,
    sigterm: Callable = None,
):
    """
    Start a loop that will run until complete
    """
    hub.pop.loop.create()
    if sigint:
        s = signal.SIGINT
        hub.pop.Loop.add_signal_handler(s, lambda s=s: asyncio.create_task(sigint(s)))
    if sigterm:
        s = signal.SIGTERM
        hub.pop.Loop.add_signal_handler(s, lambda s=s: asyncio.create_task(sigterm(s)))
    if hold:
        coros = list(coros)
        coros.append(_holder(hub))
    try:
        # DO NOT CHANGE THIS CALL TO run_forever! If we do that then the tracebacks
        # do not get resolved.
        return hub.pop.Loop.run_until_complete(asyncio.gather(*coros))
    except KeyboardInterrupt as e:
        print("Caught keyboard interrupt. Canceling...")
        hub.pop.Loop.close()


async def _holder(hub: "pop.hub.Hub"):
    """
    Just a sleeping while loop to hold the loop open while it runs until
    complete
    """
    while True:
        future = await hub.pop.loop.FUT_QUE.get()
        await future


async def await_futures(hub: "pop.hub.Hub"):
    """
    Scan over the futures that have completed and manually await them.
    This function is used to clean up futures when the loop is not opened
    up with hold=True so that ensured futures can be cleaned up on demand
    """
    while not hub.pop.loop.FUT_QUE.empty():
        future = await hub.pop.loop.FUT_QUE.get()
        await future


async def kill(hub: "pop.hub.Hub", wait: int or float = 0):
    """
    Close out the loop
    """
    await asyncio.sleep(wait)
    hub.pop.Loop.stop()
    while True:
        if not hub.pop.Loop.is_running():
            hub.pop.Loop.close()
        await asyncio.sleep(1)


async def as_yielded(hub: "pop.hub.Hub", gens: Iterable[Generator]):
    """
    Concurrently run multiple async generators and yield the next yielded
    value from the soonest yielded generator.

    async def many():
        for n in range(10):
            yield os.urandom(6).hex()

    async def run():
        gens = []
        for n in range(10):
            gens.append(many())
        async for y in as_yielded(gens):
            print(y)
    """
    fin = os.urandom(32)
    que = asyncio.Queue()
    fs = []
    to_clean = []

    async def _yield(gen):
        async for comp in gen:
            await que.put(comp)

    async def _ensure(coros):
        for f in asyncio.as_completed(coros):
            await f

    async def _set_done():
        await que.put(fin)

    def _done(future):
        to_clean.append(asyncio.ensure_future(_set_done()))

    coros = []
    for gen in gens:
        coros.append(_yield(gen))
    f = asyncio.ensure_future(_ensure(coros))
    f.add_done_callback(_done)
    while True:
        ret = await que.get()
        if ret == fin:
            break
        yield ret
    for c in to_clean:
        await c
