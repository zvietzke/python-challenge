import os
import csv

row_count = 0
total = 0
votes = {}


infile = os.path.join('Resources','election_data.csv')
outfile = os.path.join('analysis','election_data.txt')

with open(infile, 'r') as file_read:
        csv_reader = csv.reader(file_read)
        next(csv_reader)
        
        for row in csv_reader:
            name = row[2]
            if name in votes:
                 votes[name] += 1
            else:
                votes[name] = 1
            total += 1
        
winner = max(votes)


output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total votes: {total}\n"
    f"winner: {winner}\n"

)

print(output)
with open(outfile,'w') as file_write:
    file_write.write(output)        


# total votes: 369711

# charles casper stockham: 23.049% (85213)
# diana degette: 73.812% (272892)
# raymon anthony doane: 3.139% (11606)

# winner diana degette