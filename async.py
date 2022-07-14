import asyncio
from time import sleep
import requests


# async def main():
#     print("start main")
#     task = asyncio.create_task(foo("some text"))
#     print(type(task))
#     await asyncio.sleep(0.5)
#     # await task
#     print("main done")


# async def foo(text):
#     print(text)
#     await asyncio.sleep(0.5)
#     print("foo done")


# asyncio.run(main())


async def fetch_data():
    print("started fetching...")
    # await asyncio.sleep(2)
    # # sleep(2)
    for _ in range(5):
        res = requests.get("https://www.google.com")

    print("done fetching...")
    return {"status": 200}


async def print_numbers():
    for i in range(10):
        print(i)
        # await asyncio.sleep(0.25)
        sleep(0.25)


async def main():
    results = asyncio.gather(
        asyncio.to_thread(fetch_data), asyncio.to_thread(print_numbers)
    )
    print(results)


asyncio.run(main())


# you need python 3.10
