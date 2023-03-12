mylist = ['Rustem ', 'Temirgali ', 'Ruslanuly ', 'Aslan ', "Temirgali ", 'Ersultan ', 'Temirgali']

with open(r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week6\assignment\Directoriesandfiles\forlist.txt', 'w') as file:
    for x in mylist:
        file.write(x)

with open(r'C:\Users\ПК\Desktop\ruspythoh\Programming-p2\week6\assignment\Directoriesandfiles\forlist.txt', 'r') as newfile:
    result = newfile.read()
    print(result)