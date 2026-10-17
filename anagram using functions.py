'''def is_anagram(str1,str2):
    return sorted(str1)==sorted(str2)
s1=input("Enter a first string:")
s2=input("Enter a second string:")
result=is_anagram(s1,s2)
print("result=",result)'''


def is_anagram(str1,str2):
    return sorted(str1)==sorted(str2)
s1=input("Enter a first string:")
s2=input("Enter a second string:")
if is_anagram(s1,s2):
    print("the stings is anagram")
else:
    print("the strings is not anagram")
