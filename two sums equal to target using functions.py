'''def two_sums(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
numbers=list(map(int,input("Enter numbers with spaces:").split()))
target=int(input("Enter a target number:"))
result=two_sums(numbers,target)
if result:
    print("Indices:",result)
else:
    print("No value found")'''

    
def two_sums(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
numbers=list(map(int,input("Enter numbers with spaces:").split()))
target=int(input("Enter a target number:"))
result=two_sums(numbers,target)
print("result=",result)
