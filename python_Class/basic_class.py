# Python class declaration

class Person:

    #  __init__ is used as a constructor to initialize the object of this class

    def __init__(self, name):
        self.name = name

# here Person in the parenthesis represents how Inheritance works in python.
# class MDPerson inherits the Person class


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + " Esquire"

# person, doctor, lawyer are the instances of the respective class


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
#  here we access the specific attribute "name" of the person instance
print(person.name)
print(doctor.name)
print(lawyer.name)
