from itertools import cycle
n = 0
for el in cycle(["ABC", 12, 3.4]):
 if n > 12:
  break
n += 1
print(n)

