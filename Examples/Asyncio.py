import asyncio

async def tarea1():
    # Perform some operation
    await asyncio.sleep(1)
    print("tarea1 completed")

async def tarea2():
    # Perform some operation
    await asyncio.sleep(2)
    print("tarea2 completed")

async def main():
    await asyncio.gather(tarea1(), tarea2())

asyncio.run(main())
