# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output 
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
votes = {}
percentages = []
# Winning Candidate and Winning Count Tracker
winner = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(".\n", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            votes[candidate_name] = 0
        # Add a vote to the candidate's count
        votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results\n")
    print("-------------------------\n")
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    # Write the total vote count to the text file
    print(f"Total Votes: {total_votes}\n")
    print("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    # Loop through the candidates to determine vote percentages and identify the winner
    for name in candidates:

        # Get the vote count and calculate the percentage
        vote_count = votes[name]
        percentage = (vote_count / total_votes)*100
        percentages.append(percentage)

        # Print and save each candidate's vote count and percentage
        print(f"{name}: {percentage: .3f}% ({vote_count})\n")
        txt_file.write(f"{name}: {percentage: .3f}% ({vote_count})\n")

    # Generate and print the winning candidate summary
    # Find the winning candidate using percentages and indices
    win_dex = percentages.index(max(percentages))
    winner = candidates[win_dex]
    print("-------------------------\n")
    txt_file.write("-------------------------\n")
    # Save the winning candidate summary to the text file
    print(f"Winner: {winner}\n")
    txt_file.write(f"Winner: {winner}\n")
    print("-------------------------")
    txt_file.write("-------------------------")