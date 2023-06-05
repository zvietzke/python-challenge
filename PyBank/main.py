import os
import csv
#initialize variables
row_count = 0
total = 0
month_change = []
l_netchange = []
l_greatest_inc = ["",0]
l_greatest_dec = ["",999999]



infile = os.path.join('Resources','budget_data.csv')
outfile = os.path.join('analysis','budget_analysis.txt')

with open(infile,'r',encoding ='UTF-8') as file_read:
        csv_reader = csv.reader(file_read)
        next(csv_reader)
        first = next(csv_reader)
        row_count += 1
        total += int(first[1])
        previous = int(first[1])

        for row in csv_reader:
            value = int(row[1])
            row_count += 1
            total += value
            net_change = value - previous
            l_netchange.append(net_change)
            month_change.append(row[0])
            previous = value
            #two if statements to compare the next change, once for greatest increase, once for greatest decrease
            
            if net_change > l_greatest_inc[1]:
                    l_greatest_inc = [row[0], net_change]

            if net_change < l_greatest_dec[1]:
                  l_greatest_dec = [row[0], net_change]
#function to get net monthly average     

avg_change = sum(l_netchange) / len(l_netchange)

output = (
    f"Financial Analysis\n"
    f"-----------------------\n"
    f"Total months = {row_count}\n"
    f"total: ${total}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increasse in Profits: {l_greatest_inc[0]} (${l_greatest_inc[1]})\n"
    f"Greatest Decrease in Profits: {l_greatest_dec[0]} (${l_greatest_dec[1]})\n"
)

print(output)
with open(outfile,'w') as file_write:
    file_write.write(output)        

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

