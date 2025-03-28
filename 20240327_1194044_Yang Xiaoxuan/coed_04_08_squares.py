# In this script,  you will print out table with a sequncial numbers and corresponding squares numbers


# Print the table heading
print('Number\tSquare')
print('--------------')
# Print number 1 through 10 and their squares
for num in range(1,11):
    square = num**2
    print(num,'\t',square)