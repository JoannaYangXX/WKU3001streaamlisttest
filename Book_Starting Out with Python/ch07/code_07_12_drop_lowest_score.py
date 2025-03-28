# code_07_12_drop_lowest_score.py
# 7 Processing lists, In the spotlight

# Dr. LaClaire gives a series of exams during the semester in her chemistry class. At the end of the semester, she drops each student’s lowest test score before averaging the scores. She has asked you to design a program that will read a student’s test scores as input and calculate the average with the lowest score dropped. Here is the algorithm that you developed:

    # Get the student’s test scores.
    # Calculate the total of the scores.
    # Find the lowest score.
    # Subtract the lowest score from the total. This gives the adjusted total.
    # Divide the adjusted total by 1 less than the number of test scores. This is the average. 
    # Display the average.

# Program 7-12 shows the code for the program, which is divided into three functions. Rather than presenting the entire program at once, let’s first examine the main function, then each additional function separately. Here is the main function:


# This program gets a series of test scores and calculates the average of the scores with the lowest score dropped.

def main():
    # Get the test scores from the user.
    scores = get_scores()

    # Get teh total of the test scores
    total = get_total(scores)

    # Get the lowest test score
    lowest = min(scores)

    # Subtract the lowest score from the total
    total -= lowest

    # Calculate the average. Note that we divide by 1 less than the number of scores because the lowest score was dropped
    average = total / (len(scores) - 1)

    # Display the average
    print('The average, with the lowest core dropped', 'is:', average)

# the get_scores function. The function gets the test scores from the user and returns a reference to a list containing those scores. The list is assigned to the scores variable.
# the get_total function, passing the scores list as an argument. The function returns the total of the values in the list. This value is assigned to the total variable.
# the built-in min function, passing the scores list as an argument. The function returns the lowest value in the list. This value is assigned to the lowest variable.
# subtracts the lowest test score from the total variable. Then, line 21 calculates the average by dividing total by len(scores) 2 1. (The program divides by len (scores) 2 1 because the lowest test score was dropped.) Lines 24 and 25 display the average.
# Next is the get_scores function.

# Get_scores function: The get_scores function gets a series of test scores from the user and stores them in a list. A reference to the list is returned
def get_scores():
    # Create an empty list
    test_scores = []

    # Create a variable to control the loop
    again = 'y'

    # Get the scores from the user and add them in the list
    while again == 'y':
        # Get a score and add it to the list
        value = float(input('Enter a test score: '))
        test_scores.append(value)

        # What to do this again?
        print('Do you want to add another score?')
        again = input('y = yes, anything else = no: ')
        print()

    # Return the list
    return test_scores

# get_total function: The get_total function accepts a list as an argument returns the total of the values in the list
def get_total(value_list):
    # Create a variable to use as an accumulator
    total = 0.0

    # Calculate the total of the list elements.
    for num in value_list:
        total +=num

    # Return the total
    return total

# call the main function.
main()
