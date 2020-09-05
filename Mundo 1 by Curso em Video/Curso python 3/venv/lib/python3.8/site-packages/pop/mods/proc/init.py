"""
The Proc sub is used to spin up worker processes that run hub referenced
coroutines.
"""
# Import python libs
import os
import sys
import atexit
import itertools
import asyncio
import subprocess

# Import third party libs
import msgpack
import pop.hub


def __init__(hub: "pop.hub.Hub"):
    """
    Create constants used by the client and server side of procs
    """
    hub.proc.DELIM = b"d\xff\xcfCO)\xfe="
    hub.proc.D_FLAG = b"D"
    hub.proc.I_FLAG = b"I"
    hub.proc.Workers = {}
    hub.proc.WorkersIter = {}
    hub.proc.WorkersTrack = {}


def _get_cmd(hub: "pop.hub.Hub", ind, ref, ret_ref, sock_dir):
    """
    Return the shell command to execute that will start up the worker
    """
    code = "import sys; "
    code += "import pop.hub; "
    code += "hub = pop.hub.Hub(); "
    code += 'hub.pop.sub.add("pop.mods.proc"); '
    code += f'hub.proc.worker.start("{sock_dir}", "{ind}", "{ref}", "{ret_ref}")'
    cmd = f"{sys.executable} -c '{code}'"
    return cmd


def mk_proc(hub: "pop.hub.Hub", ind, workers, ret_ref, sock_dir):
    """
    Create the process and add it to the passed in workers dict at the
    specified index
    """
    ref = os.urandom(3).hex() + ".sock"
    workers[ind] = {"ref": ref}
    workers[ind]["path"] = os.path.join(sock_dir, ref)
    cmd = _get_cmd(hub, ind, ref, ret_ref, sock_dir)
    workers[ind]["proc"] = subprocess.Popen(cmd, shell=True)
    workers[ind]["pid"] = workers[ind]["proc"].pid


async def pool(
    hub: "pop.hub.Hub", num, name: str = "Workers", callback=None, sock_dir=None
):
    """
    Create a new local pool of process based workers

    :param num: The number of processes to add to this pool
    :param ref: The location on the hub to create the Workers dict used to
        store the worker pool, defaults to `hub.pop.proc.Workers`
    :param callback: The pop ref to call when the process communicates
        back
    """
    ret_ref = os.urandom(3).hex() + ".sock"
    ret_sock_path = os.path.join(sock_dir, ret_ref)
    if not hasattr(hub.proc, "Tracker"):
        hub.proc.init.mk_tracker()
    workers = {}
    if callback:
        await asyncio.start_unix_server(
            hub.proc.init.ret_work(callback), path=ret_sock_path
        )
    for ind in range(num):
        hub.proc.init.mk_proc(ind, workers, ret_ref, sock_dir)
    w_iter = itertools.cycle(workers)
    hub.proc.Workers[name] = workers
    hub.proc.WorkersIter[name] = w_iter
    hub.proc.WorkersTrack[name] = {"subs": [], "ret_ref": ret_ref, "sock_dir": sock_dir}
    up = set()
    while True:
        for ind in workers:
            if os.path.exists(workers[ind]["path"]):
                up.add(ind)
        if len(up) == num:
            break
        await asyncio.sleep(0.01)
    # TODO: This seems to be spawning extra procs, this should be fixed
    # asyncio.ensure_future(hub.proc.init.maintain(name))


async def maintain(hub: "pop.hub.Hub", name):
    """
    Keep an eye on these processes
    """
    workers = hub.proc.Workers[name]
    while True:
        for ind, data in workers.items():
            if not data["proc"].poll():
                hub.proc.init.mk_proc(ind, workers)
        await asyncio.sleep(2)


def mk_tracker(hub: "pop.hub.Hub"):
    """
    Create the process tracker, this simply makes a data structure to hold
    process references and sets them to be terminated when the system is
    shutdown.
    """
    hub.proc.Tracker = True
    atexit.register(hub.proc.init.clean)


def clean(hub: "pop.hub.Hub"):
    """
    Clean up the processes registered in the tracker
    """
    for name, workers in hub.proc.Workers.items():
        for ind in workers:
            workers[ind]["proc"].terminate()


def ret_work(hub: "pop.hub.Hub", callback):
    async def work(reader, writer):
        """
        Process the incoming work
        """
        inbound = await reader.readuntil(hub.proc.DELIM)
        inbound = inbound[: -len(hub.proc.DELIM)]
        payload = msgpack.loads(inbound, raw=False)
        ret = await callback(payload)
        ret = msgpack.dumps(ret, use_bin_type=True)
        ret += hub.proc.DELIM
        writer.write(ret)
        await writer.drain()
        writer.close()

    return work
