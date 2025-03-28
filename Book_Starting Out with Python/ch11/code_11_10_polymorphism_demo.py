# 11-10
# This program demonstrates polymorphism

import code_11_09_animals

def main():
    # Create a Mammal object, a Dog object, and a Cat object.
    mammal = code_11_09_animals.Mammal('regular animal')
    dog = code_11_09_animals.Dog()
    cat = code_11_09_animals.Cat()

    # Display information about each one
    print('The sounds they make.')
    print('_______________________')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

# the show_mammal_info function accepts an object as an argument, and calls its show_species and make_sound methods
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Call the main function
main()