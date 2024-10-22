# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("users/KP/Git/python-Challenge/PyPoll/Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("users/KP/Git/python-challenge/PyPoll/analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
vote_getters = [] # list of candidates who received votes

# Define lists and dictionaries to track candidate names and vote counts
candidate_vote_count = {} # 'candidate': vote count

# Winning Candidate and Winning Count Tracker
election_winner = ""
winning_vote_count = 0
windding_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:



        

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row


        # Get the candidate's name from the row


        # If the candidate is not already in the candidate list, add them


        # Add a vote to the candidate's count


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
