# 11-3
# This program demonstrates the Car class

import code_11_01_02_03_vehicles

def main():
    # Create an object from the Car class. The car is a 2007 Audi with 12,500 miles, priced at $21,500.00 and has 4 doors.
    used_car = code_11_01_02_03_vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Display the car's data
    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print('Number of doors: ', used_car.get_doors())

# Call the main function.
main()