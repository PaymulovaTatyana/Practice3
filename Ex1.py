import math
import statistics as s
import random

list1= [random.randrange(1, 100, 1) for i in range(10)]
print(list1)
print(math.fsum(list1))
print(s.median(list1))
print(s.stdev(list1))
