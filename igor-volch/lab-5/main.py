# class


class MyClass:
    variable = "some_text"

    def function(self):
        print("This is a message inside the class.")


my_class = MyClass()  

my_class.variable = "oop" 

print(my_class.variable)  

my_class.function()  




class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name,

            self.color,

            self.kind,

            self.value,
        )
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00


print(car1.description())
print(car2.description())




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

result = Person("Mark", 55)

print(result)



class Box:
    def __str__(self, name, age):
        self.name = name
        self.age = age

result = Person("Mark", 55)

print(result)


class Rest:
    def __repr__(self, name, age):
        self.name = name
        self.age = age

result = Person("Mark", 55)

print(result)
