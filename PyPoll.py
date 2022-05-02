# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'
#Open the elections results and read the file.
#election_data = open(file_to_load, 'r')
# To do: Perform analysis.
# Close the file.
#election_data.close()

# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #To do: Perfom analysis.
    #print(election_data)

# Add dependecies
import csv
import os
# Assign a varible for the file to load and the path.
file_to_load = os.path.join("Resources" , "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
    #Print the file object.
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('analysis' , 'election_analysis.txt')
# Use open() function with the "w" mode to write data to the file.
#open(file_to_save, 'w')

# Use open starement to open the fule as a text file.
#outfile = open(file_to_save, 'w')
# Write data to this file.
#outfile.write('Hello World')
# Close this file
#outfile.close()

# Using the with statement open the file as a text file.
with open(file_to_save, 'w') as txt_file:
    # Write title, line and three counties to the file.
   txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')


# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the csv file.
    #for row in file_reader:
        #print(row)
    # Print the header row.
    headers = next(file_reader)
    print(headers)