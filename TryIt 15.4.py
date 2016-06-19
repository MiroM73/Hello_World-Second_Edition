import random, time

t = int(time.time())

while t > (int(time.time()) - 30):
    print  random.random()
    print time.ctime()
    time.sleep(3)


