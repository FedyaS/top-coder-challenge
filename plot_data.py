import json
import matplotlib.pyplot as plt
import pandas as pd

def plot_data():
    """
    Loads data from public_cases.json and creates three scatter plots.
    """
    try:
        with open('public_cases.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: public_cases.json not found. Make sure the file is in the same directory as the script.")
        return
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from public_cases.json.")
        return

    # Extract the 'input' and 'expected_output' into a more manageable structure
    records = []
    for item in data:
        record = item['input']
        record['expected_output'] = item['expected_output']
        records.append(record)

    # Create a pandas DataFrame
    df = pd.DataFrame(records)

    # Create new features by multiplying existing ones
    df['duration_x_miles'] = df['trip_duration_days'] * df['miles_traveled']
    df['duration_x_receipts'] = df['trip_duration_days'] * df['total_receipts_amount']
    df['miles_x_receipts'] = df['miles_traveled'] * df['total_receipts_amount']
    df['all_features_product'] = df['trip_duration_days'] * df['total_receipts_amount'] * df['miles_traveled']

    # Create and save the first plot: trip_duration_days vs. expected_output
    plt.figure(figsize=(10, 6))
    plt.scatter(df['trip_duration_days'], df['expected_output'])
    plt.title('Trip Duration vs. Expected Output')
    plt.xlabel('Trip Duration (days)')
    plt.ylabel('Expected Output')
    plt.grid(True)
    plt.savefig('duration_vs_output.png')
    plt.close()
    print("Saved duration_vs_output.png")

    # Create and save the second plot: miles_traveled vs. expected_output
    plt.figure(figsize=(10, 6))
    plt.scatter(df['miles_traveled'], df['expected_output'])
    plt.title('Miles Traveled vs. Expected Output')
    plt.xlabel('Miles Traveled')
    plt.ylabel('Expected Output')
    plt.grid(True)
    plt.savefig('miles_vs_output.png')
    plt.close()
    print("Saved miles_vs_output.png")

    # Create and save the third plot: total_receipts_amount vs. expected_output
    plt.figure(figsize=(10, 6))
    plt.scatter(df['total_receipts_amount'], df['expected_output'])
    plt.title('Total Receipts Amount vs. Expected Output')
    plt.xlabel('Total Receipts Amount')
    plt.ylabel('Expected Output')
    plt.grid(True)
    plt.savefig('receipts_vs_output.png')
    plt.close()
    print("Saved receipts_vs_output.png")

    # Create and save the fourth plot: duration_x_miles vs. expected_output
    plt.figure(figsize=(10, 6))
    plt.scatter(df['duration_x_miles'], df['expected_output'])
    plt.title('Trip Duration x Miles Traveled vs. Expected Output')
    plt.xlabel('Trip Duration x Miles Traveled')
    plt.ylabel('Expected Output')
    plt.grid(True)
    plt.savefig('duration_miles_vs_output.png')
    plt.close()
    print("Saved duration_miles_vs_output.png")

    # Create and save the fifth plot: duration_x_receipts vs. expected_output
    plt.figure(figsize=(10, 6))
    plt.scatter(df['duration_x_receipts'], df['expected_output'])
    plt.title('Trip Duration x Total Receipts vs. Expected Output')
    plt.xlabel('Trip Duration x Total Receipts')
    plt.ylabel('Expected Output')
    plt.grid(True)
    plt.savefig('duration_receipts_vs_output.png')
    plt.close()
    print("Saved duration_receipts_vs_output.png")

    # Create and save the sixth plot: miles_x_receipts vs. expected_output
    plt.figure(figsize=(10, 6))
    plt.scatter(df['miles_x_receipts'], df['expected_output'])
    plt.title('Miles Traveled x Total Receipts vs. Expected Output')
    plt.xlabel('Miles Traveled x Total Receipts')
    plt.ylabel('Expected Output')
    plt.grid(True)
    plt.savefig('miles_receipts_vs_output.png')
    plt.close()
    print("Saved miles_receipts_vs_output.png")

    # Create and save the seventh plot: all_features_product vs. expected_output
    plt.figure(figsize=(10, 6))
    plt.scatter(df['all_features_product'], df['expected_output'])
    plt.title('All Features Product vs. Expected Output')
    plt.xlabel('Trip Duration x Miles Traveled x Total Receipts')
    plt.ylabel('Expected Output')
    plt.grid(True)
    plt.savefig('all_features_vs_output.png')
    plt.close()
    print("Saved all_features_vs_output.png")

if __name__ == '__main__':
    plot_data() 