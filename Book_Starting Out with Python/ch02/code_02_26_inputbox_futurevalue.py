# code_02_26_inputbox_futurevalue.py
import turtle
turtle.setup(600,600)
#num = turtle.numinput('Input', 'Enter a number', default=10, minval=0, maxval=100)
#txt = turtle.textinput('Input', 'Enter your name')
# Get the desired future value.
#future_value = float(input('Enter the desired future value: '))
# Get the annual interest rate.
#rate = float(input('Enter the annual interest rate: '))
# Get the number of years that the money will appreciate.
#years = int(input('Enter the number of years the money will grow: '))
# Calculate the amount needed to deposit.
#present_value = future_value / (1.0 + rate)**years
# Display the amount needed to deposit.
#print('You will need to deposit this amount:', present_value)

# Inputbox and futurevalue
## Input
name = turtle.textinput('Input', 'Enter your name')
future_value = turtle.numinput(
    'Input', 
    'Enter the desired future value: ', 
    default=1000, 
    minval=0, 
    maxval=1000000000)
rate = turtle.numinput(
    'Input', 
    'Enter annual interest rate: (0.01~1.00)', 
    default=0.02, 
    minval=0.01, 
    maxval=1)
year = turtle.numinput(
    'Input', 
    'Enter the number of years the money will grow: (1~10)', 
    default=1, 
    minval=1, 
    maxval=10)    

## Calculate
present_value = future_value / (1.0 + rate)**year

## Display
turtle.hideturtle()
turtle.penup()
turtle.write('Good afternnon')
turtle.setheading(270)
turtle.forward(10)
turtle.write(name)
turtle.forward(10)
turtle.write('You will need to deposit this amount: ')
turtle.forward(10)
turtle.write(f'{present_value:<10,.2f}')

print('Good afternoon %s' %name)
print('You will need to deposit this amount: %d' %present_value)
print('You will need to deposit this amount: %s' %f'{present_value:<10,.2f}')

turtle.done() 
