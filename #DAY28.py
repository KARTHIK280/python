#DAY28
#1. define subclass using threading
import threading
import time
exitFlag = 0
class myThread(threading.Thread):
    def _init_(self, threadID, name, counter):
        threading.Thread._init_(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print( "Exiting " + self.name)
def print_time(threadName, counter, delay):
     while counter:
        if exitFlag:
            threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

# 2. instantiate subclass and trigger tread
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread1.start()
thread2.start()

print("Exiting Main Thread")