#Almost any value is evaluated to True if it has some sort of content

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

'''
Any string, list, tuple, set, and dictionary are True, except empty ones

Any number is True, except 0
'''