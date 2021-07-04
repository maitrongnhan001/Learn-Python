def print_max (x, y) :
    '''Prints the maximum of the two numbers
    
    The two values must be integer'''
    x = int(x)
    y = int(y)

    if(x > y) :
        print(x, ' is maximum')
    else :
        print(y, ' is maximum')

print (print_max(3, 7))
print (print_max.__doc__)