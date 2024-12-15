def isPolindrome(string: str) -> bool:
    reverse = string[::-1]
    if string == reverse:
        return True
    return False

string = input("please enter a string: ")

if isPolindrome(string):
    print(f"{string} is a polindrome string")
else:
    print(f"{string} is not a polindrome string")