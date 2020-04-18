import os
import csv

cereal_csv = os.path.join("Resources", "cereal.csv")

with open(cereal_csv) as csvfile:

    # CSV reader delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
   
    print(csvreader)

    # Skip header
    next(csvreader, None)

    # Read each row of data after the header
    for record in csvreader:
        cereal_name = record[0]
        fiber = float(record[7])
        
        if fiber >= 5:
            print(record)
            
        
        