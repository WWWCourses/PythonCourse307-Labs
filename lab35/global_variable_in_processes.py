import multiprocessing as mp

def increment(r):
  # global x
  x = q.get()

  for _ in r:
    x+=1

  q.put(x)
  print(f"x in {mp.current_process().name}: {x}")


if __name__ == "__main__":
#   x = 0
  # create queue:
  q = mp.Queue()
  q.put(0)


  pr1 = mp.Process(target=increment, args=(range(1000),))
  pr2 = mp.Process(target=increment, args=(range(1000),))

  pr1.start();pr2.start();
  pr1.join();pr2.join();

  x = q.get()
  print(f"x in {mp.current_process().name}: {x}")
