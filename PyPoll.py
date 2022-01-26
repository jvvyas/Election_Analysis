# The daa we need to retrieve.
#1.the total number of votes cast
#2.A complete list of candidated who received votes
#3.The percentage of votes each candidate won
#4. The total number of votes each cnadiate won
#5. The winner of the election based on popular vote.

# Import the datetime class from the dateime module. 
import datetime
# Use the now() attribute on hte datetime class to get the present time. 
now =  datetime.datetime.now()
# Print the present time.
print ("The time right now is", now)

# Import the datetime class from the datetime module. 
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now + dt.datetime.now()
# print the present time.
print ( "the time right now is " , now)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file 
election_data = open(file_to_load, 'r')

# To do : perform analysis

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: perform analysis.
    print(election_data)

# Open the election results and read file
with open(file_to_load) as election_data:
    # To do: perform analysis.
    print(election_data)
    
import os
dir(Os)



print(election_data)

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:

     print(election_data)

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
print('election_data')


file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.text")
with open(file_to_save, "w") as text_file:

    text_file.write("hello World")
   
file_to_save = os.path.join("analysis", "election_analysis.text")
with open(file_to_save, "w") as text_file:

    text_file.write("hello World")
   
print = txt_file.write("Arapahoe, Denver, Jefferson")


  txt_file.write("Arapahoe")
     txt_file.write("Denver")
     txt_file.write("Jefferson")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
 txt_file.write("Arapahoe")

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")

file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
  txt_file.write("Hello World")

  txt_file.write("Arapahoe \nDenver\nJefferson")

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
  txt_file.write("Counties in the Election")

  txt_file.write("Arapahoe \nDenver\nJefferson")
  
file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Counties in the Election")
outfile.close()
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
 
  txt_file.write("Counties in the Election\n===================\nArapahoe\nDenver\nJefferson")

 
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)

    

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
file_reader = csv.reader(election_data)
headers = next(file_reader)
print(headers)

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        print(total_votes)

 

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt") 
total_votes = 0
candidate_options = []
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        candidate_options.append(candidate_name)
print(candidate_options)

for row in the file_reader:
    total_votes += 1
    candidate_name = row[2]
    if candidate_name not in candidate_options:
candidate_options.append(candidate_name)
print(candidate_options)

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
with open(file_to_load) as election_data:

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
print(candidate_votes)

if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
print(candidate_votes) 

import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
print(candidate_votes) 

candidate_votes[candidate_name] += 1

if candidate_name not in candidate_options:
candidate_options.append(candidate_name)
candidate_votes[candidate_name] = 0
candidate_votes[candidate_name] += 1
print(candidate_votes)


import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")


total_votes = 0


candidate_options = []


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

 
    headers = next(file_reader)

 
    for row in file_reader:
        
        total_votes += 1


        candidate_name = row[2]

    
        candidate_options.append(candidate_name)

print(candidate_options)


    for row in file_reader:

        total_votes += 1


        candidate_name = row[2]


        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)


print(candidate_options)

if candidate_name not in candidate_options:
           
            candidate_options.append(candidate_name)

      
            candidate_votes[candidate_name] = 0

           
            candidate_votes[candidate_name] += 1


print(candidate_votes)


if candidate_name not in candidate_options
    candidate_options.append(candidate_name)
    candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] += 1
print(candidate_votes)

candidate_votes[candidate_name] += 1

    if candidate_name not in candidate_options
        candidate_options.append(candidate_name)
        candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
print(candidate_votes)

    candidate_name = row[2]

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)  

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:

           # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

# Print the candidate vote dictionary.
print(candidate_votes)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0


# Print the candidate vote dictionary.
print(candidate_votes)

    if candidate_name not in candidate_options
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
            
            candidate_votes[candidate_votes] += 1

print(candidate_votes)


import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")


total_votes = 0


candidate_options = []

candidate_votes = {}


with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    headers = next(file_reader)

  
    for row in file_reader:
     
        total_votes += 1

       
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          
            candidate_options.append(candidate_name)

          
            candidate_votes[candidate_name] = 0



print(candidate_votes)

candidate_votes[candidate_name] += 1

if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

      
            candidate_votes[candidate_name] = 0

         
            candidate_votes[candidate_name] += 1


print(candidate_votes)

 if candidate_name not in candidate_options:


            candidate_options.append(candidate_name)

  
            candidate_votes[candidate_name] = 0


        candidate_votes[candidate_name] += 1

print(candidate_votes)

vote_percentage = (votes / total_votes) * 100

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        if candidate_name not in candidate_options:
          # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0


# Print the candidate vote dictionary.
print(candidate_votes)

         if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

  
            candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] += 1


print(candidate_votes)

if (votes > winning_count) and (vote_percentage > winning_percentage):
     winning_count = votes
     winning_percentage = vote_percentage
     winning_candidate = candidate_name


for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes) / float(total_votes) * 100

    if (votes > winning_count) and (vote_percentage > winning_percentage):
 

         winning_count = votes
         winning_percentage = vote_percentage

         winning_candidate = candidate_name

print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:

        total_votes += 1

        candidate_name = row[2]
        
   
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100


    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

# Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


