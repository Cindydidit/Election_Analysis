# The data we need to retrieve:
# 1. The total number of votes cast. CHECK
# 2. A complete list of candidates who received votes. CHECK
# 3. The percentage of votes each candidate won. CHECK
# 4. The total number of votes each candidate won. CHECK
# 5. The winner of the election based on popular vote. CHECK

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources\election_results.csv'
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #To do: Perfom analysis.
    #print(election_data)

# Add dependecies
from __future__ import print_function
import csv
import os
# Assign a varible for the file to load and the path.
file_to_load = os.path.join("Resources" , "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #Print the file object.
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis" , "election_analysis.txt")
# Use open() function with the "w" mode to write data to the file.
#open(file_to_save, 'w')

# Use open starement to open the file as a text file.
#outfile = open(file_to_save, 'w')
# Write data to this file.
#outfile.write('Hello World')
# Close this file
#outfile.close()

# Using the with statement open the file as a text file.
#with open(file_to_save, 'w') as txt_file:
    # Write title, line and three counties to the file.
   #txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')

# Initialize a total vote counter.
total_votes = 0

# Declare Candidate Options list.
candidate_options = []

# Declare a dictionary for each candidate's.
candidate_votes = {}

# Declare an empty set variable for the winning candidate.
winning_candidate = ""

# Declare and initialize a variable for the winning count.
winning_count = 0

# Declare and initialize a variable for the winning percentage.
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read/skip the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Increment total_votes variable by 1.
        total_votes += 1
        # Pull the candidate name from each row.
        candidate_name = row[2]
        # If statement to root out duplicates
        if candidate_name not in candidate_options:
            # Add candidate name to list if not duplicate.
            candidate_options.append(candidate_name)
            # Instantiate/Set tracker for the votes of each candidate to 0.
            candidate_votes[candidate_name] = 0
        # Increment each candidate's vote by one as counted.
        candidate_votes[candidate_name] += 1

# Save the election results to the text file in "w" mode.
with open(file_to_save, "w") as txt_file:
    # Assign a variable and print the electon results to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Calculate the percentage of votes each candidate received.
    # Use for loop to iterate throught the candidate_options=[] results and retreive the candidate_name from the candidate_votes{}.
    # Candidate_options loop:
    for candidate_name in candidate_votes:
        # Retreive the vote count of each candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of the votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Assign variable and print the candidates' names, vote percantage, and vote count using f-string formatting to one decimal, to the terminal.
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save candidate results to the text file.
        txt_file.write(candidate_results)
        # If statement to calculate winning count.
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            # If true than...
            # Set winning_count equal to votes.
            winning_count=votes
            # Set winning_percentage equal to vote_percentage.
            winning_percentage = vote_percentage
            # Set the the winning_candidate equal to candidate_name.
            winning_candidate=candidate_name
    # Assign a variable for and print the winning candidate summary.
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's summary to the text file.
    txt_file.write(winning_candidate_summary)
