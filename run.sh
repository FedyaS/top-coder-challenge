#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 trip_duration_days miles_traveled total_receipts_amount"
    exit 1
fi

trip_duration_days=$1
miles_traveled=$2
total_receipts_amount=$3

python solution.py "$trip_duration_days" "$miles_traveled" "$total_receipts_amount"

# TODO: Replace this with your actual implementation
echo "TODO: Implement your reimbursement calculation here"
echo "Input: $1 days, $2 miles, \$$3 receipts"
echo "Output should be a single number (the reimbursement amount)" 