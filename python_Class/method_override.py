# this program is used to demonstrate how method overriding is done in python.

class Car:
    def exclaim(self):
        print("I am car!")

# class Yug just inherits all the method from it's parent class


class Yug(Car):
    pass


class Yugo(Car):
    #  this is called method overriding. defining the same method as parent but the output is different.
    def exclaim(self):
        print("I'm a Yugo! Much like a car, but more yugo-ish.")


give_me_a_car = Car()
give_me_a_yug = Yug()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yug.exclaim()
give_me_a_yugo.exclaim()

