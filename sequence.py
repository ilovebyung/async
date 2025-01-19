import asyncio
import random

async def a():
    print("a")
    await asyncio.sleep(1)  # Simulate some work
    status = random.randint(1, 10)  # Simulate some asynchronous work
    return status

async def b(status):
    print("b")
    await asyncio.sleep(1)  # Simulate some work
    print(f"Received status from a(): {status}")

async def f():
    print("f")
    await asyncio.sleep(1)  # Simulate some work

async def g():
    print("g")
    await asyncio.sleep(1)  # Simulate some work

async def main():
    """
    This function orchestrates the execution of a() and b() in sequence.
    """
    status = await a() 
    await b(status)
    await asyncio.gather(f(), g())  # Run f() and g() concurrently

asyncio.run(main())