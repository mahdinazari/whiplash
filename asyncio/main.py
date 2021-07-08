import asyncio


async def factorial(n):
    result = 1
    print(f"""+ Started  to calculate %s""" %n)
    for i in range(1, n+1):
        result *= i
        if i % 100 ==0:
            await asyncio.sleep(0.1)

    print("- Finished to calculate %s" %n)
    return result

async def main():
    tasks = []
    requested_numbers = [5000, 2000, 100, 500]
    for number in requested_numbers:
        tasks.append(loop.create_task(factorial(number)))

    await asyncio.wait(tasks)
    return tasks


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop() #get event loop
        results = loop.run_until_complete(main()) #pass tasks to run
        for result in results:
            print('result is: \n %s' %result.result())

    except Exception as e:
        print(e)

    finally:
        loop.close()

