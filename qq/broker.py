"""
QQ task broker.
V. 0.1, Mar 16, 2013
(C) V.Hotsyk, http://github.com/hotsyk
"""

import redis

# 0.1 proof of concept, using defaults only for now
from qq import default_settings


def get_redis_connection():
    connection = redis.Redis.from_url(default_settings.QQ_BROKER_POOL[0])
    return connection
