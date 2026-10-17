'''start=int(input("Enter a starting number"))
end=int(input("Enter a ending number"))
for i in range(start,end+1):
    print("square of",i,"=",i*i)'''

\\program for armstrong number
'''num=int(input("Enter a number:"))
temp=num
digits=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**digits
    temp//=10
if sum==num:
    print("it is armstong number")
else:
    print("it is not a armstrong number")'''

\\program to find palindrome number
'''num=int(input("enter a number:"))
temp=num
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp//=10
if reverse==num:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")'''


program to find spy number
'''num=int(input("Enter a number"))
temp=num
sum=0
product=1
while temp>0:
    digit=temp%10
    sum+=digit
    product*=digit
    temp//=10
if sum==product:
    print("it is spy number")
else:
    print("not a spy number")'''


p=float(input("Enter principal amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time(years):")
amount=p*(1+r/100)**t
ci=amount-p
print("compount interest=",ci)
print("total amount=",amount)


    
    
