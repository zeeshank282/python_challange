#first import the operating system module (this will allow us to navigate, get inforamtion, read and do more things with the system files)
import os
# import a csv module as we are going to read/write over as csv file
import csv


#set a path for file; this method is used to concatenate the current working directory with the filename 'budget_data.csv'. (make sure the csv file is in the same directory as the coding script)
csvpath = os.path.join('Resources','budget_data.csv')

#open the csv file
with open(csvpath) as csvfile:
    #Identify the delimiter (which are the commas that seperate the values for date and profit) and the variable holding the contents
    csvread = csv.reader(csvfile, delimiter=',')
    
    #The next() method is used to skip the header row of the CSV file.
    next(csvread) 
    
    # creating lists for the columns 'date' and 'profit/losses'
    change_list=[]
    months = []
    profits = []
    
    # setting the starting conditions to '0' to keep track of the change in profits from month to month, as well as greatest increase and decrease in profits
    change=0
    greatest_increase = 0
    greatest_decrease = 0
    
    # a for loop is used to iterate over each row in the CSV file. The profit values are converted from strings to integers using the int() function and appended to the profits list. 
    # the month names are appended to the months list.
    for row in csvread:
        profits.append(int(row[1]))
        months.append(row[0])
        
#The profits list is converted to integers using a list comprehension.
new_profits = []
for row in profits:
    new_profits.append(int(row))
profits = new_profits

#for loop through profits indices to find greatest increase and greatest decrease
for x in range(len(profits)):
    if x < len(profits) - 1:
        change = change + (profits[x + 1] - profits[x])
        change_list.append(change)
        change = 0

#add each profits to total profits, then calculate the average change and rounding values to 2 d.p.
average_change = round(sum(change_list) / len(change_list),2)
greatest_increase = max(change_list)
greatest_decrease = min(change_list)
greatest_decrease_month = change_list.index(greatest_decrease)
greatest_increase_month = change_list.index(greatest_increase)

#set variable for greatest and least month
greatest_month = months[greatest_increase_month+1]
least_month = months[greatest_decrease_month+1]

#creates a path for output file called pybank_output
output_file = os.path.join('Analysis','pybank_analysis.txt')

#opens the output in text mode and prints the summary
with open(output_file, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------' + '\n')
    text.write('Total Months: ' + str(len(months)) + '\n')
    text.write('Total: $' + str(sum(profits)) + '\n')
    text.write('Average Change: $' + str((average_change)) + '\n')
    text.write('Greatest Increase in Profits: ' + greatest_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    text.write('Greatest Decrease in Profits: ' + least_month + ' ($' + str(greatest_decrease) + ')')

#opens the output file in readfile mode and prints
with open(output_file, 'r') as readfile:
    print(readfile.read())