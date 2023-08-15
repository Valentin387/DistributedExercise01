import asyncio

async def print_numbers():
    for i in range(1, 11):
        print(asyncio.current_task().get_name(), i)
        await asyncio.sleep(1)

async def main():
    tasks = [asyncio.create_task(print_numbers()) for _ in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
