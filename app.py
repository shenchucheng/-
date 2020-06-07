import os
from aiohttp import web


requests = []
router = web.RouteTableDef()
form = '''
<form action="/cmd" method="post" accept-charset="utf-8"
      enctype="application/x-www-form-urlencoded">
    <div>
    <label for="cmd-shutdown-set">计划关机</label>
    <input id="cmd-shutdown-set" name="cmd" type="radio" value="计划关机" autofocus/>
    </div>
    <div>
    <label for="cmd-shutdown-cancel">取消关机</label>
    <input id="cmd-shutdown-cancel" name="cmd" type="radio" value="取消关机" autofocus/>
    </div>
    <div>
    <label for=cmd-ap-set"">开启热点</label>
    <input id="cmd-ap-set" name="cmd" type="radio" value="开启热点" autofocus/>
    </div>
    <div>
    <label for="cmd-ap-cancel">关闭热点</label>
    <input id="cmd-ap-cancel" name="cmd" type="radio" value="关闭热点" autofocus/>
    </div>
    <div>
    <label for="password">密码验证</label>
    <input id="password" name="password" type="password" value=""/>
    </div>
    <input type="submit" value="运行"/>
</form>
'''

cmd = {
    "计划关机": "shutdown -s -t 60",
    "取消关机": "shutdown -a",
    "开启热点": "runas /user:administrator netsh wlan start hostednetwork",
    "关闭热点": "netsh wlan stop hostednetwork"
}


@router.get('/')
async def hello(request):
    requests.append(request)
    r = web.Response(body='<h1>Hello, 小仙女, 我是平平无奇的<a href="/cmd">电脑管家</a></h1>')
    r.content_type = "text/html;charset=utf-8"
    return r


@router.get('/cmd')
async def command(request):
    requests.append(request)
    r = web.Response(body=form)
    r.content_type = "text/html;charset=utf-8"
    return r


@router.post('/cmd')
async def command(request):
    data = await request.post()
    requests.append(data)
    cmd_name = data.get('cmd')
    cmd_text = cmd.get(cmd_name)
    if cmd_text:
        r = os.system(cmd_text)
        r = cmd_name + '：' + ('成功' if r == 0 else "失败")
    else:
        r = "命令不存在"
    return web.Response(text=r)


def main():
    app = web.Application()
    app.add_routes(router)
    web.run_app(app)


if __name__ == '__main__':
    main()
