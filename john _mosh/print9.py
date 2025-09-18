class Person:
    def walk(self):
        print("walk")

class Child1(Person):
    pass

person=Child1()
person.walk()