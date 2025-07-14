'''
#function
print("function is block of code, \n it run  when it is called, \n its used for reusebuility ")

#function syntax
def function_name(parameter1,parameter2): #functin declaraation
    print(parameter1+parameter2) #statements -- body of function
function_name(10,28) #functio calling

#nested function
def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()

#orbiditoy parameteers or arguments in function
def func(*a):
    print("printing multi value with one argument",a)
func(1,2,3,4,5)

#keyword arguments that save in dictonary
def fun(**b):
    print("printing multi value with one argument",b)
fun(a=1,b=2)
'''

#reusebuility check (imorting one code in another code and reuse)
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)