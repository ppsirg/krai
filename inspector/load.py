# -*- coding: utf-8 -*-
"""
Generate logs
"""
import psutil
from time import time
from asyncio import sleep
from aiofile import AIOFile
from datetime import datetime


async def check_server_load(settings):
    """Register server load
    """
    print(f"{settings['interval']} for load")
    await sleep(settings['interval'])
    mem = psutil.virtual_memory()
    server_load = {
        'time': time(),
        'cpu': psutil.cpu_percent(),
        'memory': {
            'percent': mem.percent,
            'used': mem.used,
            'free': mem.free,
            'buffers': mem.buffers,
            'cached': mem.cached,
        }
    }
    file_name = datetime.now().strftime(f'{settings["file_prefix"]}_%Y_%m_%d.log')
    async with AIOFile(file_name, 'a') as lg:
        await lg.write(f'{server_load}\n')
