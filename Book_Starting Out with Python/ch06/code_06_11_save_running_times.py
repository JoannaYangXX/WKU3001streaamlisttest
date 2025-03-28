# code_06_11_save_running_times.py
# 6.2 Using loops to process files

# Kevin is a freelance video producer who makes TV commercials for local businesses. When he makes a commercial, he usually films several short videos. Later, he puts these short videos together to make the final commercial. He has asked you to write the following two programs.

    # 1. A program that allows him to enter the running time (in seconds) of each short video in a project. The running times are saved to a file.
    # 2. A program that reads the contents of the file, displays the running times, and then displays the total running time of all the segments.

#Here is the general algorithm for the first program, in pseudocode:

# Get the number of videos in the project.
# Open an output file.
    # For each video in the project:
    # Get the video's running time.
    # Write the running time to the file. 
# Close the file.

def main():
    # Get the number of videos in the project
    num_videos = int(input('How many videos are in the project? '))

    # Open the file to hold the running times.
    video_file = open('video_times.txt', 'w')

    # Get each video's running time and write it to the file
    print('Enter the running times for each video.')
    for count in range(1, num_videos + 1):
        run_time = float(input('Video #' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    # Close the file
    video_file.close()
    print('The times have been saved to video_times.txt.')

# Call the main function
main()

# Program Output (with input shown in bold)
# How many videos are in the project? 6 
# Enter Enter the running times for each video. 
# Video #1: 24.5 Enter
# Video #2: 12.2 Enter
# Video #3: 14.6 Enter 
# Video #4: 20.4 Enter 
# Video #5: 22.5 Enter
# Video #6: 19.3 Enter
# The times have been saved to video_times.txt.
 