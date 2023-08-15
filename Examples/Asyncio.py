import asyncio

async def tarea1():
    # realizar alguna operación
    await asyncio.sleep(1)

async def tarea2():
    # realizar alguna operación
    await asyncio.sleep(2)

asyncio.run(asyncio.gather(tarea1(), tarea2()))