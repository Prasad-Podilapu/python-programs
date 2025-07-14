#llist

#v=[]
#print(type(v))

v=[2,5,6.8,5,'radhakrishna']
print(v)

#postive index
print(v[3])
print(v[-5])

#negative index
print(v[0:4])

#slice index [start:stop:skip]
# 2 skip means here one chatacter skiped
print(v[0:4:2])

'''
methods in list
___________________________
append
extend
count
insert
pop
remove
index
'''
#append
a=['krish','boostu',1028,'radha']
print(a)
a.append("krish")
print(a)

#extend
a.extend([56,'i live in vijayawa'])
print(a)

#count
print(a.count('krish'))

#remove
a.remove(56)
print(a)

#remove index
a.pop(5)
print(a)

#index
print(a.index('radha'))

#for
for i in [56,'i live in vijayawa']:
    print(i)
