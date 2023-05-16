#first import the operating system module (this will allow us to navigate, get inforamtion, read and do more things with the system files)
import os
# import a csv module as we are going to read/write over as csv file
import csv

#set a path for file (make sure the csv file is in the same directory as the coding script)
csvpath = os.path.join('Resources','election_data.csv')

#the csv file is opened using the with statement, and a csv.reader object is created
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    #the next function is called to skip the header row of the csv file
    next(csvread)
    
    #a dictionary called poll is created to store the name of each candidate as the key and the number of votes as the value
    poll = {}
    
    #creates list used to store candidates, vote counts, vote percent, and winner list
    number_votes = []
    candidates = []
    vote_percent = []
    winner_list = []
    
    #Set variable for total votes as a counter, starting at 0, , which will later be used to count the total number of votes cast
    total_votes = 0

    # this counts the total number of votes cast in the election, and tallies the number of votes each candidate received by incrementing the count for that candidate's name in the poll dictionary  
    for row in csvread:
        total_votes = total_votes + 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
 # this loops through each item in poll using the items() method, which returns a tuple for each key-value pair
for key, value in poll.items():
    candidates.append(key)
    number_votes.append(value)

#append vote percent
for n in number_votes:
    #round percentage to 3 d.p.
    vote_percent.append(round(n/total_votes*100, 3))

#clean_data is a list of tuples, where each tuple contains a candidate's name, number of votes they received, and their percentage of the total votes
clean_data = list(zip(candidates, number_votes, vote_percent))

#for loop to look through winner_list (which will contain the names of all the candidates) to find who received the most votes
for name in clean_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])

#makes winner_list as a string with the first entry
winner = winner_list[0]

#when there is a tie, additional winners are added into a string that is separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints to file
output_file = os.path.join('Analysis','election_analysis.txt')

with open(output_file, 'w') as text:
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write('Total Votes: ' + str(total_votes) + '\n')
    text.write('-------------------------\n')
    for entry in clean_data:
        text.write(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    text.write('------------------------- \n')
    text.write('Winner: ' + winner + '\n')
    text.write('-------------------------')

#prints file to as read file
with open(output_file, 'r') as readfile:
    print(readfile.read())