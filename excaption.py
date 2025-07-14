'''
a=1
print(b)
print(a)
'''
#the excaption handling is used that run the full code is their any error in the program 
a=5
try:
    print(b) #risky code
except:
    print("error")
else:
    print("no error")
finally:
    print("always")
print(a)