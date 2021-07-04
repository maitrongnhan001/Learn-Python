def total (a, *numbers, **phoneBook) :
    print('a: ', a)

    for simble_item in numbers :
        print('simble item is: ', simble_item)

    for first_path, second_path in phoneBook.items() :
        print(first_path, second_path)

total (1, 2, 3,  5, Nhan = 414, Nhu = 548)