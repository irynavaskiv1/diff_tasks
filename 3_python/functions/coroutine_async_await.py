import asyncio


async def count_to_three():
    print("Counter 1")
    await asyncio.sleep(0)
    print("Counter 2")
    await asyncio.sleep(0)
    print("Counter 3")
    await asyncio.sleep(0)


coroutine_counter = count_to_three()
print(coroutine_counter)  # <coroutine object count_to_three at 0x7f5a58486a98>
while True:
    try:
        coroutine_counter.send(None)
    except StopIteration:
        break
