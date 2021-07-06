name = "Swaroop"

if name.startswith('Swa') :
    print('Yes, the string starts with "Swa')

if 'a' in name :
    print('Yes, it contrains the string "a"')

if name.find('war') != -1 :
    print('Yes, it contrains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'india', 'China']
print(delimiter.join(mylist))