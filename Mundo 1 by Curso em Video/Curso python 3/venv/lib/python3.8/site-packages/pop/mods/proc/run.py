"""
Execute functions or load subs on the workers in the named worker pool
"""
# import python libs
import asyncio
import os

# Import third party libs
import msgpack
import pop.hub


async def add_sub(hub: "pop.hub.Hub", worker_name, *args, **kwargs):
    """
    Tell all of the worker in the named pool to load the given sub,

    This function takes all of the same arguments as hub.pop.sub.add
    """
    ret = {}
    workers = hub.proc.Workers[worker_name]
    for ind in workers:
        payload = {"fun": "sub", "args": args, "kwargs": kwargs}
        # TODO: Make these futures to the run at the same time
        async for chunk in hub.proc.run.send(workers[ind], payload):
            ret[ind] = chunk
    hub.proc.WorkersTrack[worker_name]["subs"].append({"args": args, "kwargs": kwargs})
    return ret


async def add_proc(hub: "pop.hub.Hub", worker_name):
    """
    Add a single process to the worker pool, also make sure that
    """
    # grab and extrapolate the data we need
    ret_ref = hub.proc.WorkersTrack[worker_name]["ret_ref"]
    sock_dir = hub.proc.WorkersTrack[worker_name]["sock_dir"]
    workers = hub.proc.Workers[worker_name]
    ind = len(workers) + 1
    for s_ind in range(len(workers) + 1):
        if s_ind not in workers:
            ind = s_ind
    hub.proc.init.mk_proc(ind, workers, ret_ref, sock_dir)
    # Make sure the process is up with a live socket
    while True:
        if os.path.exists(workers[ind]["path"]):
            break
        await asyncio.sleep(0.01)
    # Add all of the subs that have been added to processes in this pool
    for sub in hub.proc.WorkersTrack[worker_name]["subs"]:
        payload = {"fun": "sub", "args": sub["args"], "kwargs": sub["kwargs"]}
        async for chunk in hub.proc.run.send(workers[ind], payload):
            pass
    return ind


async def pub(hub: "pop.hub.Hub", worker_name, func_ref, *args, **kwargs):
    """
    Execute the given function reference on ALL the workers in the given
    worker pool and return the return data from each.

    Pass in the arguments for the function, keep in mind that the sub needs
    to be loaded into the workers for a function to be available via
    hub.proc.run.add_sub
    """
    workers = hub.proc.Workers[worker_name]
    ret = {}
    for ind in workers:
        payload = {"fun": "run", "ref": func_ref, "args": args, "kwargs": kwargs}
        # TODO: Make these futures to the run at the same time
        async for chunk in hub.proc.run.send(workers[ind], payload):
            ret[ind] = chunk
    return ret


async def set_attr(hub: "pop.hub.Hub", worker_name, ref, value):
    """
    Set the given attribute to the given location on the hub of all
    worker procs
    """
    workers = hub.proc.Workers[worker_name]
    ret = {}
    for ind in workers:
        payload = {"fun": "setattr", "ref": ref, "value": value}
        # TODO: Make these futures to the run at the same time
        async for chunk in hub.proc.run.send(workers[ind], payload):
            ret[ind] = chunk
    return ret


async def ind_func(hub: "pop.hub.Hub", worker_name, _ind, func_ref, *args, **kwargs):
    """
    Execute the function on the indexed process within the named worker pool
    """
    workers = hub.proc.Workers[worker_name]
    worker = workers[_ind]
    payload = {"fun": "run", "ref": func_ref, "args": args, "kwargs": kwargs}
    async for ret in hub.proc.run.send(worker, payload):
        return ret


async def func(hub: "pop.hub.Hub", worker_name, func_ref, *args, **kwargs):
    """
    Execute the given function reference on one worker in the given worker
    pool and return the return data.

    Pass in the arguments for the function, keep in mind that the sub needs
    to be loaded into the workers for a function to be available via
    hub.proc.run.add_sub
    """
    ind, coro = await hub.proc.run.track_func(worker_name, func_ref, *args, **kwargs)
    return await coro


async def track_func(hub: "pop.hub.Hub", worker_name, func_ref, *args, **kwargs):
    """
    Run a function and return the index of the worker that the function was
    executed on and a coroutine to track
    """
    w_iter = hub.proc.WorkersIter[worker_name]
    ind = next(w_iter)
    coro = hub.proc.run.ind_func(worker_name, ind, func_ref, *args, **kwargs)
    return ind, coro


async def gen(hub: "pop.hub.Hub", worker_name, func_ref, *args, **kwargs):
    """
    Execute a generator function reference within one worker within the given
    worker pool.

    Like `func` the sub needs to be made available to all workers first
    """
    ind, coro = await hub.proc.run.track_gen(worker_name, func_ref, *args, **kwargs)
    async for chunk in coro:
        yield chunk


async def track_gen(hub: "pop.hub.Hub", worker_name, func_ref, *args, **kwargs):
    """
    Return an iterable coroutine and the index executed on
    """
    w_iter = hub.proc.WorkersIter[worker_name]
    ind = next(w_iter)
    coro = hub.proc.run.ind_gen(worker_name, ind, func_ref, *args, **kwargs)
    return ind, coro


async def ind_gen(hub: "pop.hub.Hub", worker_name, _ind, func_ref, *args, **kwargs):
    """
    run the given iterator on the defined index
    """
    workers = hub.proc.Workers[worker_name]
    worker = workers[_ind]
    payload = {"fun": "gen", "ref": func_ref, "args": args, "kwargs": kwargs}
    async for chunk in hub.proc.run.send(worker, payload):
        yield chunk


async def send(hub: "pop.hub.Hub", worker, payload):
    """
    Send the given payload to the given worker, yield iterations based on the
    returns from the remote.
    """
    mp = msgpack.dumps(payload, use_bin_type=True)
    mp += hub.proc.DELIM
    reader, writer = await asyncio.open_unix_connection(path=worker["path"])
    writer.write(mp)
    await writer.drain()
    final_ret = True
    while True:
        ret = await reader.readuntil(hub.proc.DELIM)
        p_ret = ret[: -len(hub.proc.DELIM)]
        i_flag = p_ret[-1:]
        ret = msgpack.loads(p_ret[:-1], raw=False)
        if i_flag == hub.proc.D_FLAG:
            # break for the end of the sequence
            break
        yield ret
        final_ret = False
    if final_ret:
        yield ret
