# Election_Analysis

## Project Overview

The election commission has requested some additional data to complete the
election Audit of a recent congressional election held in the State of Colorado. Based on the data provided by one of the employee of the
Colorado Board of elections, the vote count report includes the following:

- Calculated the total number of votes cast
- Retrieved complete list of candidates who received votes
- Calculated the total number of votes each candidate received
- Calculated the percentage of votes each candidate won
- Determined the winner of the election based on popular vote


### Resources
Data Source: election_results.csv

Software used: 

Python 3.9.10, Visual Studio Code 1.38.1


### Summary
The analysis of the election data shows that:
There were 369,711 votes cast in the election.

***County Votes:***
-Arapahoe: 6.7% (24,801)
-Denver: 82.8%(306,055)
-Jefferson: 10.5% (38,855)

***Largest County Turnout:***
-Denver


### The list of Candidates:
*Charles Casper Stockham*

*Diana DeGette*

*Raymon Anthony Doane*



### The Candidate results were:
*Charles Casper Stockham* received 23% of the the votes with 85,213 votes

*Diana DeGette* received 73.8% of the the votes with 272,892 votes

*Raymon Anthony Doane* received 3.1% of the the votes with 11,606 votes


### The election Winner was:
***Diana DeGetter who received 73.8% of the votes.***



### Challenge Overview
A csv file named elections_results is used for the audit purpose. The Python in Visual Studio Code
imports the .csv data and an algorithm is set to help analyze the data and
produce the election analysis report. Visual Studio Code was used to import and
inspect the .csv file to discover it contained ballot id, election county and
candidate names data. Overall, the data was readable and there were no unusual
row values.

Through running a series of Python loops, I iterated through the 369,711 votes
cast to first discover the names of each candidate, then by creating a dictionary of
key-value pairs to calculate the number of votes each candidate received, I was
able to calculate the percentage of total votes each candidate received to
determine the winner with the highest percentage of votes.
