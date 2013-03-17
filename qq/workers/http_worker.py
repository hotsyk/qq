"""
QQ task broker.
V. 0.1, Mar 16, 2013
(C) V.Hotsyk, http://github.com/hotsyk
"""
import requests

from qq.worker import BaseWorker


class HttpWorker(BaseWorker):
    '''
    Simple http worker
    '''
    _name = 'qq-http-worker'

    def process(self, data):
        url = data['url']
        r = requests.get(url, params=data['payload'])
        return r.text


if __name__ == '__main__':
    from qq.broker import _get_redis_connection
    worker = HttpWorker(_get_redis_connection())
    worker.queue_listener()
