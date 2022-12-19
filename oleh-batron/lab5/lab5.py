# Classes

# define the MyClass class, class variable and class method
class MyClass:
    variable = "text"

    def function(self):
        print("This is a message inside the class.")


my_class = MyClass()  # create MyClass instance
my_class.variable = "oop"  # set value of the class variable to "oop"
print(my_class.variable)  # get class variable
my_class.function()  # call class method


# Learnpython.org exercise
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

# test code
print(car1.description())
print(car2.description())


# Advanced example of class usage
class Person:
    def __init__(self, name: str):
        self.name = name
        self._age = 0  # default value

    # getter function, using property decorator
    @property
    def age(self):
        print("Person getter method called")
        return self._age

    # setter function
    @age.setter
    def age(self, value: int):
        if value < 18:
            raise ValueError("Sorry your age is below eligibility criteria")
        print("Person setter method called")
        self._age = value


jack = Person("Jack")
jack.age = 20  # set jack age using setter function
print(jack.age)  # get jack age

pablo = Person("Pablo")
pablo.age = 17  # raises exception cause the age we try to set is below 18
