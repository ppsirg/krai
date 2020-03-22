# -*- coding: utf-8 -*-
from asyncio import get_event_loop, create_task
from settings import LOAD_SETTINGS, CONNECTION_SETTINGS
from inspector import register_server_load, register_server_connection


if __name__ == '__main__':
    loop = get_event_loop()
    loop.create_task(register_server_load(LOAD_SETTINGS))
    loop.create_task(register_server_connection(CONNECTION_SETTINGS))
    loop.run_forever()
