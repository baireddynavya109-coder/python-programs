num=int(input("enter a number"))
if num<=0:
    print("Invalid input")
else:
    sum=0
    for i in range(1,num):
        if num%i==0:
             sum=sum+i
    if num==sum:
            print("perfect number")
    else:
            print("not a perfect number")
