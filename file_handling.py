'''
s=open('exp.txt',mode='r')
print(s.read())
s.close()

v=open('exp.txt',mode='w')
print(v.write("hi my name is krish"))
v.close()

v=open('exp.txt',mode='a')
print(v.write(" \n i love lord krihna"))
v.close()

v=open('exp.txt',mode='r+')
print(v.read())
print(v.write(" \n r+ read and wirite"))
v.close()
'''
v=open('exp.txt','w+')
print(v.write(" wirite"))
v.seek(0)
print(v.read())
v.close()