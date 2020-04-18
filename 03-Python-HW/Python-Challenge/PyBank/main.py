# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:13:37 2020

@author: 575684
"""
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')
total = 0
total_month = 0
greatest_increase = 0
greatest_decrease = 0
biggestgain = {"date":"","value": 0}
biggestloss = {"date":"","value": 0}
prev_row = None
curr_row = None
totalchange = 0
averagechange = 0
#profloss=[]
#month=[]
with open(csvpath, encoding='utf-8', newline='') as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')
   
     
    for row in csvreader:
        
        total_month += 1  
        #if total_month == 10:
            #break
        #row = row.split(',')
        total += int(row[1])
        #greatest_increase = int(row[1])
        if prev_row is None:
            prev_row = row
            continue
        curr_row = row
        
        change = int(curr_row[1]) - int(prev_row[1])
        
        totalchange += change
       
        #
        if change < 0 and change < biggestloss["value"]:
            biggestloss["value"] = change
            biggestloss["date"] = curr_row[0]
            
        elif change > 0 and change > biggestgain["value"]:
            biggestgain["value"] = change
            biggestgain["date"] = curr_row[0]
        #profloss_col = int(row[1])

        prev_row = curr_row  
        averagechange = float(totalchange / (total_month -1))
        
print("Financial Analysis")
print("-------------------------")
print (f"Total Months:  {total_month}")
print(f"Total: ${total:,}")
print(f"Average Change: ${averagechange:,.2f}")
print(f"Greatest Increase In Profits: {biggestgain['date']} (${biggestgain['value']:,})")
print(f"Greatest Decrease In Profits: {biggestloss['date']} (${biggestloss['value']:,})")
      
#%%
#%%
# Print the results and export the data to our text file
output = os.path.join('Results','output.txt')

with open(output, "w") as txt_file:
    # Print the final vote count (to terminal)
    financial_analysis = (
        f"Financial Analysis\n"
        f"-------------------------\n"
        f"Total Months:  {total_month}\n"
        f"Total: ${total:,}\n"
        f"Average Change: ${averagechange:,.2f}\n"
        f"Greatest Increase In Profits: {biggestgain['date']} (${biggestgain['value']:,})\n"
        f"Greatest Decrease In Profits: {biggestloss['date']} (${biggestloss['value']:,})\n")
    #print(financial_analysis, end="")
    # Save the final vote count to the text file
    txt_file.write(financial_analysis)
   

     