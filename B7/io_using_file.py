from os import linesep


f = open('./B7/poem.txt', 'w')
f.write("today sky is beautiful!!")
f.close()

f = open('./B7/poem.txt')
while True:
    line = f.readline()
    if(len(line) == 0) : 
        break
    print(line)
f.close()