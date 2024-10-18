# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/kp/Git/python-challenge/PyBank/Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/kp/Git/python-challenge/PyBank/analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
greatest_increase = ("", 0)
greatest_decrease = ("", 9999999999999999999)
net_change_list = []
date_of_change = []


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Loop through and process each row of data
    for row in reader:

        # Track the total months
        total_months += 1

        # Track the total net
        total_net += int(row[1])

        # Calculate the average net change across the months
        # Have to calcuate net_change prior to updated previous_net
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        date_of_change.append(row[0])

        # Calculate the greatest increase in profits
        if net_change > greatest_increase[1]:
            greatest_increase = (row[0], net_change)

        # Calculate the greatest decrease in losses
        if net_change < greatest_decrease[1]:
            greatest_decrease = (row[0], net_change)


    # Calculate the average change amount
    average_change = sum(net_change_list) / len(net_change_list)
    average_change = f"{average_change:.2f}"



# Set variable to hold all the lines / data for analysis


output = (

    # Print analysis header
    f"Financial Analysis\n"

    #print line break
    f"**************************\n"

    # Print Total Number of Months
    f"Total months: {total_months}\n"

    #Print Total Net amount
    f"Total: ${total_net}\n"

    #Print Average Change Amount
    f"Average Change: ${average_change}\n"

    # Print the greatest increase in profits (date and amount) over the entire period
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"

    # Print the greatest decrease in losses (date and amount) over the entire period
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"

)


# Print the output
print(output)


# Code used to check the calculations as I was working through the code
# print(sum(net_change_list))
# print(len(net_change_list))


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
