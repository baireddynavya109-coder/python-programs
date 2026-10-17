'''s=input("enter sting:")
lower=upper=0
for ch in s:
    if ch in s.lower():
        lower+=1
    if ch in s.upper():
        upper+=1
print("upper letters:",upper)
print("lower letters:",lower)

s=input("Enter string:")
count=0
vowels="aeiouAEIOU"
for ch in s:
    if ch in vowels:
        count+=1
print("number of vowels:",count)


n=int(input("Enter number:"))
temp=n
sum=0
product=1
while temp>0:
    digit=temp%10
    sum+=digit
    product*=digit
    temp//=10
if sum==product:
    print("spy numbers")
else:
    print("not spy number")'''


n=int(input("enter N:"))
nums=list(map(int,input("enter numbers:").split()))
total=n*(n-1)//2
missing=total-sum(nums)
print("missing number:",missing)


