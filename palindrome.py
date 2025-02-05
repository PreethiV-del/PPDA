def is_palindrome(string):
    string = string.lower()
    left, right = 0, len(string) - 1
    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True 
name = input("Enter a string: ")
if is_palindrome(name):
    print(f"'{name}' is a palindrome")
else:
    print(f"'{name}' is not a palindrome.")
