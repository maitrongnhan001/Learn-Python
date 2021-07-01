while True:
    s = input('Enter someting: ')
    if s == 'quit' :
        break
    if len(s) < 3:
        print('too small')
        continue
    print('Length of the string is: ', len(s))
    
print('Done')