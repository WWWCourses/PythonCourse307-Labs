import time

def sum_squares(start, end):
  global sum
  for i in range(start,end):
    sum += i**2



start = time.perf_counter()
sum = 0

sum_squares(1,2_500_000)
sum_squares(2_500_000, 5_000_000)

print(sum)
end = time.perf_counter()
print(end - start)