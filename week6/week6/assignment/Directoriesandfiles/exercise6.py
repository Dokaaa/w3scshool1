import os 


# for x in range(65, 91):
#     result = open(chr(x)+'.txt', 'x')

# #! for delete all this files:

for y in range(65, 91):
    os.remove(chr(y)+'.txt')