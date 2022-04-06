#! /usr/local/bin/python3.6

import time
import json
import asyncio
from datetime import datetime
from pprint import pprint

import aiohttp


URL = 'https://192.168.1.57/apiv1/devices'
PAYLOAD = {
    'phone':'989187710445',
    'udid' :'2b6f0cc904d137be2e1730235f5664094b831186',
    'bankId':'2'
}

HEADER = {
    'Authorization':'eyJhbGciOiJIUzI1NiIsImlhdCI6MTU0NzYzODMyMiwiZXhwIjoxNTc5'
    'MTc0MzIyfQ.e30.dHyLtCJ9KqQXgvgpgD0jZ11Dl9GWkb3lc60lTW_rdPo'
}

VERB = 'CLAIM'
VERIFY_SSL=False


def time_calculator(start_time, end_time):
    total_time = end_time - start_time
    return total_time.total_seconds()


async def worker(session, url, method, data, headers):
    number_of_requests = 0
    while number_of_requests < 1:
        request_start_time = datetime.now()
        async with session.request(
            method=VERB,
            verify_ssl=VERIFY_SSL,
            url=URL,
            data=PAYLOAD,
            headers=HEADER
        ) as response:
            request_end_time = datetime.now()
            request_total_time = time_calculator(
                request_start_time,
                request_end_time
            )
            number_of_requests += 1
        return (response.status, request_total_time)


async def main():
    start_time = datetime.now()
    async with aiohttp.ClientSession() as session:
        func = [
            worker(session, URL, method=VERB, data=PAYLOAD, headers=HEADER) \
        for i in range(550)
        ]
        result = await asyncio.gather(*func)
        end_time = datetime.now()
        pprint(result)
        total_time = time_calculator(start_time, end_time)
    print('Time taken for tests: ', total_time)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

