# -*- coding: utf-8 -*-

server_list = [
    'https://www.google.com',
    'https://bitbucket.org',
    'https://es.wikipedia.org',
    'https://outlook.live.com/owa/'
]

LOAD_SETTINGS = {
    'file_prefix': 'status',
    'interval': 0.25,
    'cpu': True,
    'memory': True,
}
CONNECTION_SETTINGS = {
    'file_prefix': 'connectivity',
    'interval': 5,
    'checks': server_list
}
