import pickle

shopListFiles = './B7/shoplist.data'
shoplist = ['apple','mongo','carrot']

f = open(shopListFiles, 'wb')

pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shopListFiles, 'rb')
strorelist = pickle.load(f)

print(strorelist)
f.close()