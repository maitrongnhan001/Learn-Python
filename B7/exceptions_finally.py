import sys
import time

f = None

try :
    f = open("poem.txt")

    while True :
        line = f.readline()

        if(len(line) == 0) :
            break
        print(line, end = " ")
        sys.stdout.flush()
        print('Press cril + C now')
        time.sleep(5)
except EOFError :
    print('Could not find file poem.txt')
except KeyboardInterrupt :
    print("!! You cancelled the reading from the file.")
finally :
    if f :
        f.close()
    print('Cleaning up: Close the file')