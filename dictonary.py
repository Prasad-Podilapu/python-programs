#a={}
#print(type(a))

'''

d={'a':123,'1':"abc"}
print(d)
print(d['a'])
print(d['1'])




#metods

#get,kesy,values,items
d={'a':123,1:"abc"}
print(d.get('a'))
print(d.get(1))
print(d.keys())
print(d.values())
print(d.items())
d.update({2:'boostu'})
print(d.items())
'''
d={'a':123,1:"abc"}

#keys
for i in {'a':123,1:"abc"}:
    print(i)

#keys
#for j in {'a':123,1:"abc"}.keys():
 #   print(j)

#values
#for j in {'a':123,1:"abc"}.values():
 #   print(j)
#keys and values
for j in {'a':123,1:"abc"}.items():
    print(j)