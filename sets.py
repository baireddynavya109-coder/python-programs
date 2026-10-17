'''#sets
s1={2,3,4,90,100}
s2={2,3,4,90}
s3={1,3,5,7}
s1.add(101)
print(s1)
print(s2.union(s3))
print(s3.intersection(s1))'''


s1={2,3,4,90,100}
s2={2,3,4,90}
s3={1,3,5,7}
s1.add(101)
print(s1)
print(s2.union(s3))
print(s3.intersection(s1))
print(len(s1))
print(s1.difference(s3))
s3.clear()
print(s3)
print(set("students"))
s={'a','b','c','d'}
for i in s:
    print(i)
