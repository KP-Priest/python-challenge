# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join(r"/users/kp/Git/python-challenge/PyPoll/Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join(r"/users/kp/Git/python-challenge/PyPoll/analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
# Define lists and dictionaries to track candidate names and vote counts
candidate = ""  # holds candidate name
candidate_list = [] # list of candidates who received votes
votes = {} # 'candidate': candidate's vote count
total_votes = 0  # Track the total number of votes cast
outcome = "" #candidates final vote tally

# Winning Candidate and Winning Count Tracker
election_winner = "" #holds election winner candidate name
winning_vote_count = 0 #winning candidate's total votes
winning_percentage = 0 #percentage of total votes each candidate received

# Open the CSV file and process it
with open(file_to_load, 'r') as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print("^ ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate_name from the row
        candidate = row[2] 

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            votes[candidate] = 0

            # Add a vote to the candidate's count
        votes[candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}\n")

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in votes:
        # Get the vote count and calculate the percentage
        vote_count = votes[candidate]
        vote_percentage = f"{(vote_count / total_votes) * 100:.3f}%"
        # Update the winning candidate if this one has more votes
        if vote_count > winning_vote_count:
            winning_vote_count = vote_count
            election_winner = candidate
        outcome += f"{candidate}: {vote_percentage} ({vote_count})\n"
    
    # Compile the election outcome summary data
    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"{outcome}\n"
        f"-------------------------\n"
        f"Winner: {election_winner}\n"
    )
        
    # Prints all required data to the terminal    
    print(output)
        
# Writes the winning candidate summary to csv file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# End of script
