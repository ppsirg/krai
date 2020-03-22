# -*- coding: utf-8 -*-
"""
pip install aiohttp
"""
import aiohttp
from aiofile import AIOFile
from time import time as tm
from datetime import datetime
from asyncio import sleep, get_event_loop, gather
from concurrent.futures import ProcessPoolExecutor


async def ping(session, url):
    """Ping a url to determine connection availability and quality.
    """
    start_time = tm()
    try:
        async with session.get(url) as response:
            resp_text = await response.text()
            response = {
                'url': url,
                'code': response.status,
                'lenght': len(resp_text),
                'time': tm() - start_time,
                'timestamp': datetime.now().strftime('%Y_%m_%d-%H:%M:%S')
                }
    except Exception as e:
        response = {
            'url': url,
            'code': None,
            'lenght': None,
            'time': tm() - start_time,
            'timestamp': datetime.now().strftime('%Y_%m_%d-%H:%M:%S')
            }
    return response


async def check_connectivity(settings):
    """Register server connectivity.
    """
    timeoutLapse = settings['interval']
    await sleep(settings['interval'])
    print(f"{settings['interval']} for connection")
    try:
        timeout = aiohttp.ClientTimeout(total=timeoutLapse)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            pings = [ping(session, url) for url in settings['checks']]
            results = await gather(*pings)
    except TimeoutError as err:
        print(f'el ping falló por timeout: {err}')
        now = datetime.now().strftime('%Y_%m_%d-%H:%M:%S')
        results = [
            {'url': url, 'code': 502, 'length': 0,'time': timeoutLapse, 'datetime': now}
            for url in settings['checks']
            ]
    except Exception as err:
        print(f'el ping falló porque: {err}')
        now = datetime.now().strftime('%Y_%m_%d-%H:%M:%S')
        results = [
            {'url': url, 'code': 502, 'length': 0,'time': 0, 'datetime': now}
            for url in settings['checks']
            ]
    finally:
        file_name = datetime.now().strftime(f'{settings["file_prefix"]}_%Y_%m_%d.log')
        async with AIOFile(file_name, 'a') as lg:
            await lg.write(f'{results}\n')
        print(['{url}: [{code}]'.format(**a) for a in results])
