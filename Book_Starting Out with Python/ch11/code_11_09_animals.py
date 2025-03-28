# 11-9
# The Mammal class represents a generic mammal.
class Mammal:
    # The __init__ method accepts an argument for the mammal's species.
    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message indicating the mammal's species
    def show_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's way of making a generic sound
    def make_sound(self):
        print('Grrrrr')
    
    # then test code_11_09_01_test.py

# The Dog class is a subclass of the Mammal class.
class Dog(Mammal):
    # The __init__ method calls the cuperclass's __init__method passing 'Dog' as the species
    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # The make_sound method overrides the superclass's make_sound method
    def make_sound(self):
        print('Woof! Woof!')

    # then test code_11_09_02_test.py
        
# The Cat class is a subclass of the Mammal class.
class Cat(Mammal):
    # the __init__ method calls the superclass's __init__method passing 'Cat' as the species
    def __init__(self):
        Mammal.__init__(self, 'Cat')

    # the make_sounnd method overrides the superclass's make_sound method
    def make_sound(self):
        print('Meow')
    
    # then test code_11_09_03_test.py