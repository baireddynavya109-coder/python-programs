'''for i in range(1,21):
    print(i,"->",i*i)'''


nums=list(map(int,input("Enter number:").split()))
for n in nums:
    if n%3==0:
        print(n)
         
