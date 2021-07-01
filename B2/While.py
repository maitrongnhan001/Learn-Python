number = 23
runing = True

while runing:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("Congretulations, you guessed it.")
        runing = False
    elif guess < number:
        print('No. It is a little higher than that')
    else:
        print('No. It is a little lower than that')
    
    print('Done')
    

