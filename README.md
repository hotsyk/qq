qq
==

QQ is simple task queue based on the redis with the aim to be HA and realiable task management queue.

Idea behind QQ is that developer should define his own task worker (router) for execution of every task he need and easch worker will run as any number of independent daemons on any remote servers, having only pool of redis servers as the common queue to exchane data between tasks.

v. 0.1, Mar 16: proof of concept
---------------------------------

* Base task router
* Http task router with the ability to make GET requests to the given url
* Router registration - ability to run routers as daemons and specify number of desired daemons
* Connection to redis
* Sending data to desired router
* Get data executed

v. 0.1.1
-------------------------
* Connection to the pool of redis servers
* Sending data to desired router to redis with the round-robin selection of the server in pool
* Getting result of the task
