#!/usr/bin/env python


#Abstract 
class Animal(object):
    def __init__(self, name):
        self.name = name

    def cen_eat(self, food):
        pass
    
    def eat(self, food):
        pass
    
    def speak(self):
        pass
    
    def die(self):
        print self.name, "lived a good life"

    def __str__(self):
        return self.__class__.__name__+ ":" + self.name

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, "Mrs. "+ name)

    def can_eat(self, food):
        returfood.lower() == "fish"

    def eat(self, food):
        print self.name, "sniffs", food

    def speak(selF):
        print self.name + ": meow"

class Dog(Animal):
    def can_eat(self, food):
        return True

    def eat(self, food):
        print self.name, "gobbles", food

    def speak(self):
        print self.name + ": woof"
    
    



dog = Dog("Rover")
cat = Cat("Pretty")

print isinstance(dog, Dog)
print isinstance(dog, ANimal)
print isinstance(cat, Cat)
print isinstance(cat, Animal)
print isinstance(cat, Dog)

print dog
print cat

