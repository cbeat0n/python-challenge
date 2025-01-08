# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
months = []
net_change_list = []    # List to track the changes in the PnL for each month to month, like changes Jan to Feb (tracked as Feb)
greatestprofits = 0     # List the greatest profits
greatestprofitsmonth = ""   # List the month that stored the greatest profits
greatestlosses = 0          # List the greatest losses
greatestlossesmonth = ""    # List the month that stored the greatest losses


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    months.append(first_row[0])
    # Track the total and net change
    total_months = 1
    total_net = total_net + int(first_row[1])
    

    # Process each row of data
    for row in reader:

        # Track the total
        total_months = total_months + 1
        months.append(row[0])
        # Track the net change
        total_net = total_net + int(row[1])
        
        if total_months == 2:
            net_change_list.append(int(row[1]) - int(first_row[1]))
        else:
            net_change_list.append(int(row[1]) - last_pnl)

        # Calculate the greatest increase in profits (month and amount)
        greatestprofits = max(net_change_list)
        greatestprofitsmonth = months[net_change_list.index(greatestprofits) + 1]
        # Calculate the greatest decrease in losses (month and amount)
        greatestlosses = min(net_change_list)
        greatestlossesmonth = months[net_change_list.index(greatestlosses) + 1]

        last_pnl = int(row[1]) #Set the last row's PnL to a value before next for loop interation.




# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_net_change: .2f}
Greatest Increase in Profits: {greatestprofitsmonth} (${greatestprofits})
Greatest Decrease in Profits: {greatestlossesmonth}  (${greatestlosses})"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
