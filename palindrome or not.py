def is_palindrome(s):
    s=s.lower()
    rev=""
    for ch in s:
        rev=ch+rev
    return s==rev
string=input("enter a string:")
if is_palindrome(string):
    print("palindrome")
else:
    print("not palindrome")
