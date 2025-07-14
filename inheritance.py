#inheritance in python and their types
'''
#single inheritance
class parent():
    def output(self):
        print("\ni am the parent")
class child(parent):
    def outputc(self):
        print("i am child")
x=child()
x.output()
x.outputc()

#multilevel inheritance
class p1():
    def out1(self):
        print("\n\ngrand father of p3 and father of p2")
class p2(p1):
    def out2(self):
        print("father of p3 and son of p1")
class p3(p2):
    def out3(self):
        print("son of p2,and grand son of p1")
y=p3()
y.out1()
y.out2()
y.out3()
'''
'''
#multiple inhertiance
class fat():
    def outf(self):
        print("i am father")
class mot():
    def outm(self):
        print("i am mother")
class child(fat,mot):
    def outc(self):
        print("i am student")
z=child()
z.outf()
z.outm()
z.outc()
'''
#hieraxhical inheritance
class fat():
    def out(self):
        print("i am father of two childs")
class child1(fat):
    def outc1(self):
        print("i am first child")
class child2(fat):
    def outc2(self):
        print("i am sencond child")

c=child1()
c.out()
c.outc1()
b=child2()
b.out()
b.outc2()