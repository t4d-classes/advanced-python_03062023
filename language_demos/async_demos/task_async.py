""" single async """

import asyncio
from random import randint

def delay() -> float:
    """ delay """
    return randint(1,10) / 2


async def get_data(task_num: int = 0) -> int:
    """ get data """
    print(f"start get data: {task_num}")
    await asyncio.sleep(delay())
    print(f"end get data: {task_num}")
    return task_num


async def main() -> None:
    """ main """
    # coroutine_obj = get_data()
    # print(type(coroutine_obj))

    # task_obj = asyncio.create_task(coroutine_obj)
    # await asyncio.sleep(1)
    # print("task object created")
    # print(type(task_obj))

    # await task_obj

    def all_done(t: asyncio.Task):
        print(f"all done : task {t.result()}")

    task1 = asyncio.create_task(get_data(1))
    # task2 = asyncio.create_task(get_data(2))

    task1.add_done_callback(all_done)
    # task2.add_done_callback(all_done)

    #await task1
    # while not task1.done():
    #     await asyncio.sleep(0.1)

    # print("a")
    # await get_data(1)
    # print("b")


    # def print_b(t):
    #     print("b") 
    
    # print("a")
    # task1 = asyncio.create_task(get_data(1))
    # task1.add_done_callback(print_b)

    # task1.result
       


    # await asyncio.sleep(1)

    # await task1
    # await task2

if __name__ == "__main__":
    asyncio.run(main())