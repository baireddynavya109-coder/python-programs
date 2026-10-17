'''p=float(input("Enter principal amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time(years):"))
amount=p*(1+r/100)**t
ci=amount-p
print("compount interest=",ci)
print("total amount=",amount)'''


'''text=input("Enter a string:")
vowels=0
consonants=0
digits=0
for ch in text:
    if ch.isdigit():
        digit+=1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
print("vowels=",vowels)
print("consonants=",consonants)
print("digits=",digits)'''



'''n=int(input("Enter a number:"))
for i in  range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()'''

n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
