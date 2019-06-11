#create file paths across operating system
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print (csvpath)

#initialize title and rows as lists
Header = [] 
rows = []

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    #initialize Total Months
    TotalMonths = 0

    #skip header
    Header = next(csvreader)
    
    # extracting each data row one by one
    for row in csvreader: 
        rows.append(row)
        TotalMonths = TotalMonths + 1
    # get total number of rows /dates
    print("Total no. of rows: %d"%(csvreader.line_num))
    # printing the field names 
    print('Header Fields: ' + ', '.join(Header for Header in Header)) 
    # Print Total Months
    print(f"Total Months = {int(TotalMonths)}")
  
    #  printing first 5 rows 
    print('\nFirst 5 rows are:\n') 
    for row in rows[]: 
    # parsing each column of a row 
        for col in row: 
            print("%s"%col), 
        print('\n')
       
    
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