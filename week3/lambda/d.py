def myfunc(n):
  return lambda a : a * n #11*2

mydoubler = myfunc(2)

print(mydoubler(11))