'''n=int(input("enter n value"))
sum=0.0
for i in range(1,n+1):
    sum+=1/i
print("the sum of series:",sum)'''



'''n=int(input("enter n value"))
sum=0.0
for i in range(1,n+1):
    sum+=1/i
print("the sum of series:",round(sum,3))'''




'''n1,n2,n3,n4=map(int,input("enter 4 integers:").split())
print(n1,n2,n3,n4,sep="")

#the split() method handles space or newline seperation between inputs.
#the map(int, ...)coverts the string inputs to integers
#the 'sep=""' arguments  ensures no space is placed between the values.'''




'''count=0
for i in range(1,501):
    if i%2==0 and i%3==0:
        print(i,end=" ")'''


#covert height in feet and inches to cm.
#[1 feet =12 inches and 1 inch=2,54 cm]
#(sample input:2 feet 7 inch
#sample output:78.74 cm)
#prompt the user to input their height.

'''print("input your height:")
feet=int(input("feet: "))
inches=int(input("inches:" ))
#convert the height from feet to inches and add to inches.
inches+=feet*12
#calculate the height in centimeters by multiplying by the conversation fault.
h_cm=inches*2.54
#print the calculated heiht in centimeters.
print("height in cm is:",h_cm)'''

#print numbers from 0 to 100 except the multiples of 4 and 6
'''for i in range(1,101):
    if i%4!=0 and i%6!=0:
        print(i,end=" ")'''

#fibonacci series
'''nterms=int(input("enter number of terms"))
n1,n2=0,1
count=0
while count<nterms:
    print(n1,end=" ")
    next=n1+n2
    n1=n2
    n2=next
    count+=1'''

s=[1,4,6,3,7,9,40,45,23,54,21,32]
for i in s:
    if i%2==0:
        print(i)


