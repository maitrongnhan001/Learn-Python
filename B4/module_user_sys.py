import sys

print ('The command line argument is:')

for i in sys.argv:
    print (i)

print ('\n\nThe PYTHONPATH is: ', sys.path, '\n')