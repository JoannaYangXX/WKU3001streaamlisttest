# Set maximum temperature(100)
Max_temp = 100  
# Get the substance's temperature
temp = float(input("Enter current temperature of sustances: "))
# As long as necessary,  give instruct the user to adjust the temrmostat. 

# If the temperature is too high(Max temp >)and less than 5 mins display the message
while temp > Max_temp:
    # Instruction is to diaplay the following message
    # Turn the thermostat down and wait 5 mins
    print("Turn the thermostat down and wait 5 mins")
    # Then take the temperature again and enter it
    print("Then take the temperature again and enter it")
    # Ask the current temperature
    temp = float(input("What is the current temperature:"))
# Display "All temperature is in normal parameter"
print("All temperature is in normal parameter")