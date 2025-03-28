# code_06_12_read_running_times.py
# 6.2 Using loops to process files

#Kevin is a freelance video producer who makes TV commercials for local businesses. When he makes a commercial, he usually films several short videos. Later, he puts these short videos together to make the final commercial. He has asked you to write the following two programs.

    # 1. A program that allows him to enter the running time (in seconds) of each short video in a project. The running times are saved to a file.
    # 2. A program that reads the contents of the file, displays the running times, and then displays the total running time of all the segments.

# Here is the general algorithm for the first program, in pseudocode:

# Initialize an accumulator to 0. 
# Initialize a count variable to 0. 
# Open the input file.
# For each line in the file:
    #Convert the line to a floating-point number. (This is the running time for a video.) 
    # Add one to the count variable. (This keeps count of the number of videos.) 
    # Display the running time for this video.
    # #Add the running time to the accumulator.
# Close the file.
# Display the contents of the accumulator as the total running time.

def main():
    # Open the video_times.txt file for reading.
    video_file = open('video_times.txt', 'r')

    # Initialize an accumulator to 0.0
    total = 0.0

    # Initialize a variable to keep count of the video.
    count = 0

    print('Here are the running times for each video: ')

    # Get the values from the file and total them.
    for line in video_file:
        # Convert a line to a float
        run_time = float(line)

        # Add 1 to the count variable
        count += 1

        # Display the time
        print('Video #', count, ': ', run_time, sep = "")

        # Add the time to total
        total += run_time

    # Close the file
    video_file.close()

    # Display the total of the running times.
    print('The total running time is', total, 'seconds.')

# Call the main function
main()

# Program Output
# Here are the running times for each video: 
# Video #1: 24.5
# Video #2: 12.2
# Video #3: 14.6
# Video #4: 20.4
# Video #5: 22.5
# Video #6: 19.3
# The total running time is 113.5 seconds.
