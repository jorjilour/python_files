class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")


    def draw(self):
        print("draw")


point1 = Point(10, 20)


point1.draw()

point1.x = 11
point1.y = 23

point2 = Point(30,26)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


john = Person("John")
john.talk()

### INHERITANCE


class Mammal:

    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_annoying(self):
        print("its annoying")




