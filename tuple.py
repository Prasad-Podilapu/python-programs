#tuple

b=()
print(type(b))

a=(3,5,6,9)

#index
print(a[-1])

#slicing
print(a[0:3])

print(min(a))
print(max(a))
print(sum(a))
print(len(a))

#operation

#conctenation
t1=(1,3,5)
t2=(2,4,6)

print(t1+t2)

#repetion
c=(6,2)
print(c*11)

for i in t1:
    print(i)


#membership
print(1 in t2)

print(1 not in t2)

print(t1 is t2)

print(t1 is not t2)