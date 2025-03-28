# code_07_25_bar_chart2.py
# 7.10 Plotting List Data with the matplotlib Package
## Plotting a bar chart
### Customizing the bar width
#### This program displays a simple bar chart

import matplotlib.pyplot as plt
def main():
    # Create a list with the X coordinates of each bar's left edge.
    left_edges = [0,10,20,30,40]

    # Create a list with the hights of each bar
    heights = [100,200,300,400,500]

    # Create a variable for the bar with
    bar_width = 5

    # Build the bar chart
    plt.bar(left_edges, heights, bar_width)

    # Display the bar chart
    plt.show()

# Call the main function
main()