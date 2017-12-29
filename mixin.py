
"""
Mixins are a sort of class that is used to "mix in" extra properties and methods into a class.
This allows you to create a class in a compositional style.
"""

class BaseClass(object):
    def test0(self):
        print ('MyBaseClass')

class Mixin1(object):
    def test1(self):
        print ("Mixin1")

class Mixin2(object):
    def test2(self):
        print ("Mixin2")


class MyClass(Mixin2, Mixin1, BaseClass):
    pass


if __name__ == '__main__':
    obj = MyClass()
    obj.test1()
    obj.test2()
    obj.test0()