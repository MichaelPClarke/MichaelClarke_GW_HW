# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:37:59 2020

@author: 575684
"""
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
total = 0
Khan_count = 0
Correy_count = 0
Li_count = 0
Otooley_count = 0
winner = ["Khan", "Correy", "Li", "O'Tooley"]

with open(csvpath, encoding='utf-8', newline='') as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        total += 1
        candidateX = row[2]
    
        if candidateX == "Khan":
            Khan_count += 1
        elif candidateX == "Correy":
            Correy_count += 1
        elif candidateX == "Li":
            Li_count += 1
        elif candidateX == "O'Tooley":
            Otooley_count += 1
        
        otooley_total = int(Otooley_count) / int(total)
        o_total = float(round(otooley_total * 100))
        Khan_total = int(Khan_count) / int(total)
        k_total = float(round(Khan_total * 100))
        Li_total = round(Li_count) / int(total)
        l_total = float(round(Li_total * 100))
        Correy_total = round(Correy_count) / int(total)
        c_total = float(round(Correy_total * 100))
        
        if Khan_count > Correy_count and Khan_count > Otooley_count and Khan_count > Li_count:
            winner = ("Khan")
        elif Correy_count > Otooley_count and Correy_count > Li_count:  
            winner = ("Correy")
        elif Otooley_count > Li_count:
            winner = ("O'Tooley")
        else:
            winner = ("Li")
        
print(f"Election Results")
print("-------------------------------")   
print(f"Total Votes: {total}")
print("-------------------------------")
print(f"Khan: {k_total: .3f}% ({Khan_count})")
print(f"Correy: {c_total: .3f}% ({Correy_count})")
print(f"Li: {l_total: .3f}% ({Li_count})")
print(f"O'Tooley: {o_total: .3f}% ({Otooley_count})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

#%%
# Print the results and export the data to our text file
output = os.path.join('Results','output.txt')

with open(output, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total}\n"
        f"-------------------------\n")
   #print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    # Determine the winner by looping through the counts
    voter_output = (
        f"Khan: {k_total: .3f}% ({Khan_count})\n"
        f"Correy: {c_total: .3f}% ({Correy_count})\n"
        f"Li: {l_total: .3f}% ({Li_count})\n"
        f"O'Tooley: {o_total: .3f}% ({Otooley_count})\n")
   #print(voter_output)  
        # Save each candidate's voter count and percentage to text file
    txt_file.write(voter_output)
    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
   #print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)        

