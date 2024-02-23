# encoding:UTF-8

import asyncio
import time
c = True


async def a():
    global c
    a = 0
    while (c == True):
        a = a + 1
        print(f'a{a}')
        await asyncio.sleep(0.1)


async def b():
    global c
    a = 0
    while (a <= 5):
        a = a + 1
        print(f'b{a}')
        await asyncio.sleep(0.1)
    c = False
    return a


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(a()),
    asyncio.ensure_future(b()),
]
c = loop.run_until_complete(asyncio.gather(*tasks))
print(f'end:{c[1]}')
