import threading
numbers = [0,1,2,3,4,5,6,7,8,9]
my_lock = threading.Lock()
#my_lock = threading.Semaphore()

def my_func():
    global numbers 
    for _ in range(100000):
        #my_lock.acquire()
        if my_lock.locked:
            with my_lock:
                for i in range(len(numbers)):
                    if i == len(numbers) - 1:
                        numbers[i] += numbers[i] - numbers[i-1]+1

                    else:
                        numbers[i] += numbers[i+1] - numbers[i]
        #my_lock.release()

thread1 = threading.Thread(target=my_func)
thread2 = threading.Thread(target=my_func)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(numbers)