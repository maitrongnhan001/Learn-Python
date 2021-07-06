from typing import overload


shopList = ['apple', 'mongo', 'carrot', 'banana']

print('i have ', len(shopList), ' item to purchase')

print('the item are: ', end=' ')
for i in shopList :
    print(i, end=' ')

print('\nalso have to buy rice.')
shopList.append('rice')
print('My shopping list is now: ', shopList)

print('The first item i will buy is: ', shopList[0])
oldItem = shopList[0]
del shopList[0]
print('i bought the', oldItem)
print('My shoping list is now', shopList)