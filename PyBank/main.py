#create file paths across operating system
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
print (csvpath)

#initialize csvlist
csvlist = []

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV DictReader to read the csv file into an ordered dictionary
    csvreader = csv.DictReader(csvfile, delimiter=',')
    print(csvreader)

# Reading csvdictreader file into a list of ordered dict & printing TotalMonths
    for row in csvreader:
        csvlist.append(row)
TotalMonths = len(csvlist)
#print(csvlist)
#print(type(csvlist))
print("""
Financial Analysis
----------------------------
""")
print(f"Total Months: {TotalMonths} ")

# Calculating the sum of Profit/Loss, Average of Changes, Greatest Inc & Dec of Profits & printing all
SumProfitLosses = 0
PreviousMonthProfitLoss = 0
SumofChange = 0
ChangeBetweenMonth=0
FirstRun=1
GreatestInc = {
    "Date": "",
    "Change": 0
}
GreatestDec = {
    "Date": "",
    "Change": 0
}

for row in csvlist:
        #print(row['Profit/Losses'])
        SumProfitLosses = SumProfitLosses + int(row['Profit/Losses'])
        if FirstRun==1:
            PreviousMonthProfitLoss = int(row['Profit/Losses'])
            FirstRun=0
        else:
          ChangeBetweenMonth= int(row['Profit/Losses'])-PreviousMonthProfitLoss
          SumofChange=SumofChange+(ChangeBetweenMonth)
          PreviousMonthProfitLoss= int(row['Profit/Losses'])
          if ChangeBetweenMonth > GreatestInc["Change"]:
              GreatestInc["Date"] = row['Date']
              GreatestInc["Change"] = ChangeBetweenMonth

          elif ChangeBetweenMonth < GreatestDec["Change"]:
              GreatestDec["Date"] = row['Date']
              GreatestDec["Change"] = ChangeBetweenMonth

            


print(f"Total: $ {SumProfitLosses}")

AverageChange = SumofChange / (TotalMonths - 1)
print(f"Average  Change: $ {round(AverageChange, 2)}")
print(f"Greatest Increase in Profits: {GreatestInc['Date']} ( ${GreatestInc['Change']})")
print(f"Greatest Decrease in Profits: {GreatestDec['Date']} ( ${GreatestDec['Change']})")
        

       
    
#------------------ WRITE O/P INTO NEW FILE------------------------

# Specify the file to write to
output_path = os.path.join(".", "Output", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
        
    txtfile.write("""Financial Analysis
----------------------------
    \n""")
    txtfile.writelines(f"Total Months: {TotalMonths} \n")
    txtfile.writelines(f"Total: $ {SumProfitLosses} \n")

    txtfile.writelines(f"Average  Change: $ {round(AverageChange, 2)}\n")
    txtfile.writelines(f"Greatest Increase in Profits: {GreatestInc['Date']} ( ${GreatestInc['Change']})\n")
    txtfile.writelines(f"Greatest Decrease in Profits: {GreatestDec['Date']} ( ${GreatestDec['Change']})\n")
        

