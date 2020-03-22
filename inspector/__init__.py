# -*- coding: utf-8 -*-
from .connectivity import check_connectivity
from .load import check_server_load

async def register_server_connection(settings):
    """Register server connectivity.
    """
    while True:
        await check_connectivity(settings)


async def register_server_load(settings):
    """Register server load
    """
    while True:
        await check_server_load(settings)
