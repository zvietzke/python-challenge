import os
import csv
#initialize variables
row_count = 0
total = 0


infile = os.path.join('Rescources','election_data.csv')
outfile = os.path.join('analysis','budget_analysis.txt')

with open(infile, 'r') as file_read:
        csv_reader = csv.reader(file_read)
        next(csv_reader)
        first = next(csv_reader)
        




          


output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"\n"

)

print(output)
with open(outfile,'w') as file_write:
    file_write.write(output)        


# total votes: 369711

# charles casper stockham: 23.049% (85213)
# diana degette: 73.812% (272892)
# raymon anthony doane: 3.139% (11606)

# winner diana degette