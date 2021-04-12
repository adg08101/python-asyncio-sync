import asyncio


async def waiter(lock):
    await lock.acquire()
    print('waiting for it ...')
    lock.release()
    # await lock.wait()
    # print('... got it!')

async def waiter1(lock):
    await duerme()
    # lock.acquire()
    print('... got it!')
    # lock.release()

async def duerme():
    await asyncio.sleep(1)

async def main():
    # Create an Event object.
    # event = asyncio.Event()
    lock = asyncio.Lock()

    # Spawn a Task to wait until 'event' is set.
    asyncio.gather(
        waiter(lock),
        waiter1(lock),
        # return_exceptions=False
        return_exceptions=True
    )

    # Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    # lock.acquire()
    # print('waiting for it ...')
    # lock.release()
    # event.set()

    # Wait until the waiter task is finished.
    # await waiter_task
    # await waiter_task1

if __name__ == '__main__':
    asyncio.run(main())

"""
# lock

lock = asyncio.Lock()

# ... later
await lock.acquire()
try:
    # access shared state
finally:
    lock.release()

# condition

cond = asyncio.Condition()

# ... later
await cond.acquire()
try:
    await cond.wait()
finally:
    cond.release()
    
# Semaphore

sem = asyncio.Semaphore(10)

# ... later
await sem.acquire()
try:
    # work with shared resource
finally:
    sem.release()
"""