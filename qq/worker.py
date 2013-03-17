"""
QQ task broker.
V. 0.1, Mar 16, 2013
(C) V.Hotsyk, http://github.com/hotsyk
"""
import ast


class BaseWorker(object):
    """
    Base class for workers.
    _name is being used as identifier of the worker and router.
    Worker will listen for queue with his name
    """

    _name = 'qq-worker'
    _connection = None

    def __init__(self, connection, name=None):
        self._connection = connection
        self._name = name or self._name

    def queue_listener(self):
        """
        Queue listener. After apperaring of the message in the queue,
        process is called
        """
        while True:
            # listen until smth appears
            job = ast.literal_eval(self._connection.brpop(self._name, 0)[1])
            self.process(job)

    def process(self, data):
        """
        Actual actions will be done here
        Base worker do some simple adding, described in data as
        data = {'0': value1, '1': value2}
        """

        variable1 = int(data['0'])
        variable2 = int(data['1'])

        return variable1 + variable2


if __name__ == '__main__':
    from qq.broker import _get_redis_connection
    worker = BaseWorker(_get_redis_connection())
    worker.queue_listener()
