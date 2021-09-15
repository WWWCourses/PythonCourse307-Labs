import time
import multiprocessing as mp

def sum_squares(start, end):
  sum = q.get()

  for i in range(start,end):
    sum += i**2

  q.put(sum)

start = time.perf_counter()
# sum = 0
# create queue
q = mp.Queue()
q.put(0)

# create processes
pr1 = mp.Process(target=sum_squares, name="Pr1", args=(1,2_500_000))
pr2 = mp.Process(target=sum_squares, name="Pr2", args=(2_500_000, 5_000_000))


# start processes
pr1.start()
pr2.start()

# wait for proceses to finish
pr1.join()
pr2.join()

sum = q.get()
print(sum)
end = time.perf_counter()
print(end - start)