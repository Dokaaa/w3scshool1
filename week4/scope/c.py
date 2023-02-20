x = 300 # x here is global

def myfunc():
  print(x)

myfunc()

print(x)