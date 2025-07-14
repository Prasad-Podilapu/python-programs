'''
#set datatype
a={1,2,3,4}
print(type(a))

#do not allow duplicates 
b={1,2,2,5}
print(b)

#no indexing and un orderd

c={9,5,6,6,7,'abc'}
#print(a[1])  run time will come because it does not support index
print(c) #it will print randomly because it is un orderd 

#metods
s={5,6,7,3,8,9}
print(s)

#1.add()
s.add(1028)
print(s)

#update()
s.update({32,66,77,88})
print(s)

#pop()
s.pop() #it delete randomly

#remove()
s.remove(6)
print(s)
'''

#set operators
set1={1,2,3,4}
set2={3,5,6,4}
print(set1,set2)

#union
print(set1.union(set2))

#intersection
print(set1.intersection(set2))

#difference
print(set1.difference(set2))

#superset
ex1={1,2,3,4,5}
ex2={1,2,3,4}
print(ex1.issuperset(ex2))
print(ex1.issubset(ex2))
print(ex2.issubset(ex1))

#for loop
x={2,3,6,7,8,9}
for i in x:
    print(i)
