import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

# 这里用的是老代码，现在可以用async 代替@asyncio.coroutine，用await代替yield from。
# async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
async def init(loop):
        app = web.Application(loop=loop)
        app.router.add_route('GET', '/', index)
        srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
        logging.info('server started at http://127.0.0.1:9000...')
        return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

# 详解
# https://blog.csdn.net/q381907223/article/details/80991600