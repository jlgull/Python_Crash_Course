"""
Classes work from Python_Crash_Course book

"""

class Dog():
    """A Simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name  = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in respnse to the command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in respnse to the command."""
        print(self.name.title() + " rolled over.")


my_dog = Dog("willie", 6)

print("My dog's name is " + my_dog.name.title() + ".")

print(dir(Dog))
print(dir(my_dog))