#encapulation:
#       wrapping of varaible and methods in a single unit is called encapulation using
# 1. private __   it can not access by the other classes
# 2. public 
# 3. protected _   it only access by the inherted classes
'''
class demo():
    def __init__(self,a,b):
        self.__a=a #private
        self._b=b #protected
class demo2(demo):
    def ouput(self):
        #pritn(self.__a)  it can not access by this class
        print(self._b)
d=demo2(2,3)
d.ouput()
'''