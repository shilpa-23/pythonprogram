class time:

    def __init__(self,hour=10,min=35,sec=60):


     def printtime(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.min, time.sec))


t = time()
t.hour = 12
t.min = 30
t.sec = 00
time.printtime(t)
t.printtime()