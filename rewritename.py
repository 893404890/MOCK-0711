import json

import mitmproxy
from mitmproxy import ctx
from mitmproxy.http import flow

class RewriteName:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if 'https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=' in flow.request.pretty_url:
            ctx.log.info(f'{flow.response.text}')
            ctx.log.info(str(flow.response.text))
            data=json.loads(flow.response.text)
            for i in range [0,4]:
                data['data']["items"][i]["name"]='zx001'+str(i)
            flow.response.text=json.dumps(data)


addons=[
    RewriteName()
]
if __name__ == '__main__':
    print(__file__)
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p','8080','-s',__file__])