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






 

 
