
#Return the 7 first characters of the file:
f = open("demofile.txt", "r")
print(f.readline().strip())
f.close()
print(f.closed)

#! we can use numbers like index od the text