import threading 
data = [1,2,3,4,5]
result = []
threads = []

def process_item(item):
    result.append(item**2)

for item in data:
    thread = threading.Thread(target=process_item, args=(item,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(result)