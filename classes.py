class Animal(object):
    """Basic attributes of an animal"""

    def __init__(self, name, height=0.0, length=0.0):
        self.height = height
        self.length = length
        self.name = name

    def __str__(self):
        return "I'm a %s." % self.name


""" Program entry when running """
if __name__ == "__main__":
    cat = Animal("Cat", 5.2, 10.2)
    print(cat)

    dog = Animal("Dog", 10.5, 25.7)
    print(dog)
