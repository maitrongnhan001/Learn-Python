def reverse (text) :
    return text[::-1]

def is_palindrome(text) :
    return text == reverse(text)

something = input('Enter your input: ')
print(reverse(something))
if(is_palindrome(something)) :
    print("Yes, it is a palindrome")
else :
    print("Yes, it is not a palindrome")