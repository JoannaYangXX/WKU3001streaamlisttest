# code_07_21_line_graph3.py
# 7.10 Plotting List Data with the matplotlib Package
## Ploting a line graph
### Customizing the X and Y axes
#### This program displays a simple line graph
import matplotlib.pyplot as plt

def main():
    # Create lists with the X and Y coordinates of each data point
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]

    # Build the line graph
    plt.plot(x_coords, y_coords)

    # Add a title
    plt.title('Sample Data')

    # Add labels to the axes
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')

    # Set the axis limits
    plt.xlim(xmin=-1, xmax = 10)
    plt.ylim(ymin=-1, ymax = 6)

    # Add a grid
    plt.grid(True)

    # Display the line graph
    plt.show()

# Call the main function
main()