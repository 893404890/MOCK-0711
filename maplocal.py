
import mitmproxy
from mitmproxy import  http


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """

        if 'https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=' in flow.request.pretty_url:
            with open('namemodify.json', encoding='utf-8') as f:
                flow.response=http.HTTPResponse.make(200,f.read())
addons=[
    Events()
]
if __name__ == '__main__':
    print(__file__)
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p','8080','-s',__file__])