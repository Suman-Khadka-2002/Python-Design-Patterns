class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    """
    The factory method.
    """
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
'''
In this example, the get_pet() method acts as a factory for creating Dog and Cat objects.
The pet parameter specifies the type of object to create, and the method returns an instance
 of the appropriate class. This allows the caller of the get_pet() method to create objects 
without having to know the exact class that will be created.
'''