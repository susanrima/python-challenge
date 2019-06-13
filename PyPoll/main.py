#create file paths across operating system
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
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
TotalVotes = len(csvlist)
#print(csvlist)
#print(type(csvlist))


print("""
Election Results
-------------------------
""")
print(f"Total Votes: {TotalVotes} ")
print("""
-------------------------
""")


CandidateListofDict=[]

found_candidate=0

for row in csvlist:
    found_candidate=0
    for CandidateDict in CandidateListofDict:
        if row["Candidate"] == CandidateDict["Candidate"]:
            #print('in')
            #print(CandidateDict.keys())
            CandidateDict['NumberOfVotes'] = CandidateDict['NumberOfVotes'] + 1
            found_candidate=1
    if found_candidate==0:
        CandidateListofDict.append({"Candidate" : row["Candidate"],"NumberOfVotes" : 1})
        #print(CandidateListofDict)


#print(CandidateListofDict)

# Specify the file to write to
output_path = os.path.join(".", "Output", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
    
    print("""Election Results
        ----------------------------
        """)
    print(f"Total Votes: {TotalVotes}")
    txtfile.write("""Election Results
        ----------------------------
        \n""")
    txtfile.writelines(f"Total Votes: {TotalVotes} \n")

    for CandidateDict in CandidateListofDict:
        

        print(f"{CandidateDict['Candidate']}:  {round(float(CandidateDict['NumberOfVotes']/TotalVotes * 100), 3)}  % ({CandidateDict['NumberOfVotes']}))")


        
        txtfile.writelines(f"{CandidateDict['Candidate']}:  {round(CandidateDict['NumberOfVotes']/TotalVotes * 100, 3)}  % ({CandidateDict['NumberOfVotes']}) \n")



    

    







'''
    "Candidate1":
}
'''
'''
CandidateList = []
CandidateName = "Name"

for row in csvlist:
    #print(row['Candidate'])
CandidateName = row['Candidate']
    print(CandidateName)
    if CandidateName != 
CandidateList.append(CandidateName)


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
 '''       

