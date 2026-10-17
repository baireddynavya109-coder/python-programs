'''n=int(input("Enter numbers:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

year=int(input("enter year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year")


list=[1,2,3,4,5]
target=int(input("Enter target:"))
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if(list[i]+list[j]==target):
            print(list[i],list[j])

p=float(input("Enter principal:"))
t=float(input("Enter time:"))
r=float(input("Enter rate:"))
si=p*t*r
print("simple interest=",si)

s=input("Enter string:")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")'''

username=input("Enter username:")
password=input("Enter password:")
if username=="admin" and password=="1234":
    print("login successful")
else:
    print("invalid credentials")


