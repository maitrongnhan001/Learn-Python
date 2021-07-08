try :
    text = input('Enter something -->')
    text += 1
except EOFError :
    print('Why did you do an EOF on me?')
except KeyboardInterrupt :
    print('You cancelled the operation.')
except :
    print('this is number')
else :
    print('you enter: {}'.format(text))