# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:13:37 2020

@author: 575684
"""
import os
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
     