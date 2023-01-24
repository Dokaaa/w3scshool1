def myfunc():
  global x #the variable belongs to the global scope
  x = "fantastic"

myfunc()

print("Python is " + x)