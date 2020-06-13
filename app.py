#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# File Name: test.py
# Author: Shechucheng
# Created Time: 2020-06-07 00:15:54


import os
import asyncio
from aiohttp import web
from locale import getdefaultlocale


requests = []
encoding = 'gbk' if 'cp936' in getdefaultlocale() else 'utf-8'


cmd = {
    "计划关机": "shutdown 1",  # 分钟
    "取消关机": "shutdown -c",
    "立即关机": "shutdown 0",
    "重新启动": "shutdown -r",
    "文件管理": ""
        } if os.name == 'posix' else {
    "计划关机": "shutdown -s -t 60", # 秒
    "取消关机": "shutdown -a",
    "立即关机": "shutdown -s -t 0",
    "文件管理": ""
}


async def command(request):
    data = await request.post()
    requests.append(data)
    cmd_name = data.get('cmd')
    cmd_text = cmd.get(cmd_name)
    if cmd_text:
        try:
            p = await asyncio.create_subprocess_shell(cmd_text, 
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.STDOUT)
            out, err = await p.communicate()
            r = out.decode(encoding=encoding)
            status_code = p.returncode
        except:
            status_code = os.system(cmd_text)
            r = cmd_text
        status = True if status_code == 0 else False
    else:
        r = '命令不存在'
        status = None

    return web.json_response({"status": status, "info": r})


async def index(request):
    raise web.HTTPFound('/index.html')



def main():
    if os.name != 'posix':
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_static('/', 'static')
    app.router.add_post('/cmd', command)
    web.run_app(app, port=8080)


if __name__ == "__main__":
    main()
     
