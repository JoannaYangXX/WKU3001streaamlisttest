# You have to write a python program that get three score and calculate average score.Set high_score as 95, then compare to the high_socre, if the users average score is higher than high_score,show congratulation message with current score,otherwise display current socre

# Set high_score
# Get score1
# Get score2
# Get score3
# Calculate the average socre
# Determine whether the average score is higher than high_score.If the average score is greater than high_score
    # display high sore and user's aveage score with congralution messsage
# Otherwise
    # Display the current average score

# Set high_score
high_score = 95

# Get scores from the user
score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))

# Calculate the average score
average_score = (score1 + score2 + score3) / 3

# Determine whether the average score is higher than high_score
if average_score > high_score:
    print(f"Congratulations! Your average score is {average_score:.2f}, which is higher than the high score of {high_score}!")
else:
    print(f"Your average score is {average_score:.2f}. Keep working hard!")