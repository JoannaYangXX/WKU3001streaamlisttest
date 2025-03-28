# code_04_14_validation1.py
# Get a test score.
score = int(input('Enter a test score: '))
# Make sure it is not less than 0. 
while score < 0:
    print('ERROR: The score cannot be negative.') 
    score = int(input('Enter the correct score: '))