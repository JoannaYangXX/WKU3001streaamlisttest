# code_03_06_grader1.py
# This program gets a numeric test score from the
# user and displays the corresponding letter grade.
# Named constants to represent the grade thresholds 
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test
score = int(input('Enter your test score: '))
# Determine the grade. 
if score >= A_SCORE:
    print('Your grade is A.') 
else:
    if score >= B_SCORE: 
        print('Your grade is B.')
 #       print('You need', A_SCORE - score, 'more score to get A grade')
    else:
        if score >= C_SCORE:
            print('Your grade is C.') 
        else:
            if score >= D_SCORE: 
                print('Your grade is D.')
            else:
                print('Your grade is F.')