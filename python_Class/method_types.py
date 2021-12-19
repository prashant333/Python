# This program is used to demonstrate types of methods in a class
# There are three types of methods, instance method, class method, static method.

class A:
    count = 0

    def __init__(self):
        A.count += 1

    @staticmethod
    def exclaim():
        print("I'm A")

    @classmethod
    def Kids(cls):
        print("A has", cls.count, "little objects")


easy_a = A()
breezy_a = A()
wheezy_a = A()
breezy_a.exclaim()
A.Kids()
