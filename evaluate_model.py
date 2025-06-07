import json
import subprocess
import pandas as pd

from solution2 import calculate_reimbursement

def run_solution(trip_duration_days, miles_traveled, total_receipts_amount):
    cmd = [
        "python", "solution.py",
        str(trip_duration_days),
        str(miles_traveled),
        str(total_receipts_amount)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0 or not result.stdout.strip():
        print(f"--- Error running solution.py ---")
        print(f"Inputs: days={trip_duration_days}, miles={miles_traveled}, receipts={total_receipts_amount}")
        print(f"Return Code: {result.returncode}")
        if result.stdout:
            print(f"Stdout: {result.stdout}")
        if result.stderr:
            print(f"Stderr: {result.stderr}")
        print("---------------------------------")
        return 0.0  # Return a default value to continue evaluation

    return float(result.stdout.strip())

def evaluate():
    with open('public_cases.json', 'r') as f:
        cases = json.load(f)

    results = []
    for case in cases:
        inputs = case['input']
        trip_duration_days = inputs['trip_duration_days']
        miles_traveled = inputs['miles_traveled']
        total_receipts_amount = inputs['total_receipts_amount']
        
        expected_output = case['expected_output']
        # actual_output = run_solution(trip_duration_days, miles_traveled, total_receipts_amount)
        actual_output = calculate_reimbursement(trip_duration_days, miles_traveled, total_receipts_amount)
        error = abs(expected_output - actual_output)
        
        results.append({
            'trip_duration_days': trip_duration_days,
            'miles_traveled': miles_traveled,
            'total_receipts_amount': total_receipts_amount,
            'expected': expected_output,
            'actual': actual_output,
            'error': error
        })

    df = pd.DataFrame(results)
    
    exact_matches = df[df['error'] <= 0.01].shape[0]
    close_matches = df[df['error'] <= 1.00].shape[0]
    average_error = df['error'].mean()
    
    print(f"Total cases: {len(cases)}")
    print(f"Exact matches (±$0.01): {exact_matches} ({exact_matches / len(cases):.2%})")
    print(f"Close matches (±$1.00): {close_matches} ({close_matches / len(cases):.2%})")
    print(f"Average error: ${average_error:.2f}")

if __name__ == "__main__":
    evaluate() 