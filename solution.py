import sys
import json
import math

def calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount):
    
    # Per Diem Calculation
    per_diem_rate = 100
    per_diem = per_diem_rate * trip_duration_days
    
    # 5-day trip bonus (Lisa's interview)
    if trip_duration_days == 5:
        per_diem += 50

    original_miles_traveled = miles_traveled
    # Mileage Calculation (tiered)
    mileage_reimbursement = 0
    remaining_miles = miles_traveled
    
    if remaining_miles > 500:
        mileage_reimbursement += (remaining_miles - 500) * 0.35
        remaining_miles = 500
    if remaining_miles > 100:
        mileage_reimbursement += (remaining_miles - 100) * 0.45
        remaining_miles = 100
    mileage_reimbursement += remaining_miles * 0.58

    # Efficiency Bonus (Kevin's interview)
    if trip_duration_days > 0:
        miles_per_day = original_miles_traveled / trip_duration_days
        if 180 <= miles_per_day <= 220:
            mileage_reimbursement += 25 * trip_duration_days

    # Receipt Reimbursement
    receipt_reimbursement = total_receipts_amount
    
    # Penalty for small receipts on multi-day trips
    if trip_duration_days > 1 and total_receipts_amount < 20:
        receipt_reimbursement = 0

    # Spending penalties (Kevin's interview)
    if trip_duration_days > 0:
        daily_spending = total_receipts_amount / trip_duration_days
        if trip_duration_days <= 3 and daily_spending > 75:
            receipt_reimbursement = min(total_receipts_amount, trip_duration_days * 75)
        elif 4 <= trip_duration_days <= 6 and daily_spending > 120:
            receipt_reimbursement = min(total_receipts_amount, trip_duration_days * 120)
        elif trip_duration_days > 6 and daily_spending > 90:
            receipt_reimbursement = min(total_receipts_amount, trip_duration_days * 90)
            
    # Rounding bonus for .49 and .99 (Lisa's interview)
    cents = round(total_receipts_amount * 100) % 100
    if cents == 49 or cents == 99:
        receipt_reimbursement += 1

    total_reimbursement = per_diem + mileage_reimbursement + receipt_reimbursement
    
    return round(total_reimbursement, 2)

if __name__ == "__main__":
    trip_duration_days = int(sys.argv[1])
    miles_traveled = float(sys.argv[2])
    total_receipts_amount = float(sys.argv[3])
    
    reimbursement = calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount)
    
    print(reimbursement) 