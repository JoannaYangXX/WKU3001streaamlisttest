# code_07_23_line_graph5.py
# 7.10 Plotting List Data with the matplotlib Package
## Ploting a line graph
### Displaying markers at the data points
#### This program displays a simple line graph

import matplotlib.pyplot as plt

def main():
    # Create lists with the X and Y coordinates of each data point
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]

    # Build the line graph
    plt.plot(x_coords, y_coords, marker='o')

    # Add title
    plt.title('Sales by Year')

    # Add labels to the axes
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customize the tick marks
    plt.xticks([0,1,2,3,4],
               ['2016','2017','2018','2019','2020'])
    plt.yticks([0,1,2,3,4,5],
               ['$0m','1$m','2$m','3$m','4$m','5$m'])

    # Add a grid
    plt.grid(True)

    # Display the line graph
    plt.show()

# Call the main function
main()