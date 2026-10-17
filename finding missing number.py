n=int(input("enter N:"))
nums=list(map(int,input("enter numbers").split()))
total=n*(n+1)//2
missing=total-sum(nums)
print("missing number:",missing)
