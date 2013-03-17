"""
QQ task broker.
V. 0.1, Mar 16, 2013
(C) V.Hotsyk, http://github.com/hotsyk
"""

import redis
import random

# 0.1 proof of concept, using defaults only for now
from qq import default_settings


def _get_redis_connection(server_uri=None):
    """
    get connection to redis
    """
    connection = redis.Redis.from_url(server_uri or
                                      default_settings.QQ_BROKER_POOL[0])
    return connection


class Broker(object):

    _connection = None
    _connection_pool = None

    def __init__(self, connection):
        """
        For 0.1 we have only 1 redis connection
        """
        self._connection = connection
        self._connection_pool = None

    def select_next(self, current):
        """
        get selection to next redis server instead of current
        """
        self._connection = self._connection_pool[random.randint(0,
                                                 len(self._connection_pool))]
        return self._connection

    @classmethod
    def get_redis_connection(cls,
                             server_settings=default_settings.QQ_BROKER_POOL):
        """
        get connection to redis server using round robin
        for 0.1 server [0] is always used
        """
        return _get_redis_connection()

    def _send_task(self, queue, raw_data, result=False):
        """
        Raw interface to send data to the redis queue
        """
        self._connection.lpush(queue, raw_data)

    def send_task(self, connection, router_name, data):
        """
        General interface to send task to the queue
        """
        return self._send_task(router_name, data)


