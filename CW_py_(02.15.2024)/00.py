import threading
import time


def worker_function():
    print("running program")
    n = 0
    for i in range(99999999):
        n += i%3

    #time.sleep(1)
    print("finished running", n)
thread = threading.Thread(target=worker_function)

thread.start()
print("main thread")
exit()
#thread.join()