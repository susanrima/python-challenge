#create file paths across operating system
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print (csvpath)

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #budget_data_list = list(csvreader)
    Date = []
    ProfitLoss = []

    print(csvreader)
    #print(budget_data_list)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Read each row and count total months
    TotalMonths = 0
    NetAmount = 0
    for row in csvreader:
        #print(row)
        TotalMonths = TotalMonths + 1
        #NetAmount += int(row[2])
        Date.append(row[1])
        ProfitLoss.append(row[1])

    print(f"Total Months = {int(TotalMonths)}")
    print(Date[0])
   # print(f"Net Amount = {int(NetAmount)}")
       
    
#------------------ WRITE O/P INTO NEW FILE------------------------

# Specify the file to write to
#output_path = os.path.join(".", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #csvwriter.writerow(['Total Months', 'Total', 'Average  Change', 'Greatest Increase in Profits','Greatest Decrease in Profits'])

    # Write the second row
    #csvwriter.writerow(['Caleb', 'Frost'])