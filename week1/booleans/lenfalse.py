class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

'''
One more value, or object in this case, evaluates to False
if you have an object that is made from a class with a __len__ function 
that returns 0 or False

'''