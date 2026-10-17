def add(a,b):
    return a+b
t=int(input("Enter a number of test cases:"))
for i in range(t):
      a=int(input("Enter first number:"))
      b=int(input("Enter second number:"))
      print("sum=",add(a,b))
