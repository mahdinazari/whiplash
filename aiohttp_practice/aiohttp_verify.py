#! /usr/local/bin/python3.6

import asyncio
from datetime import datetime
from pprint import pprint

import aiohttp


PINBLOCK_ENCODE='CAB647238BC898DD'
URL = 'http://192.168.1.57:81/apiv1/tokens/203/codes/'+PINBLOCK_ENCODE+'?primitive=yes'
VERB = 'VERIFY'


def time_calculator(start_time, end_time):
    total_time = end_time - start_time
    return total_time.total_seconds()


async def claim_worker(session, url, method):
    request_start_time = datetime.now()
    async with session.request(
        method=VERB,
        url=URL,
    ) as response:
        request_end_time = datetime.now()
        request_total_time = time_calculator(
            request_start_time,
            request_end_time
        )
        return (response.status, request_total_time)


async def main():
    start_time = datetime.now()
    async with aiohttp.ClientSession() as session:
        func = [
            claim_worker(
                session,
                url=URL,
                method=VERB,
            )
            for i in range(80)
        ]
        result = await asyncio.gather(*func)
        end_time = datetime.now()
        pprint(result)
        total_time = time_calculator(start_time, end_time)
    print('Time taken for tests: ', total_time)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

