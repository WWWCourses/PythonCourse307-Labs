import time
import threading

def sum_squares(start, end):
  lock.acquire()
  global sum
  for i in range(start,end):
    sum += i**2
  lock.release()


start = time.perf_counter()
sum = 0
# create a lock
lock = threading.Lock()

# create threads
thread1 = threading.Thread(target=sum_squares, name="Tr1", args=(1,2_500_000))
thread2 = threading.Thread(target=sum_squares, name="Tr1", args=(2_500_000, 5_000_000))


# start threads
thread1.start()
thread2.start()

# wait for threads to finish
thread1.join()
thread2.join()

print(sum)
end = time.perf_counter()
print(end - start)