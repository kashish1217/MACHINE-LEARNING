import csv
import random

# Parameters
rows = 20
cols = 5

with open("random_data.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write header
    header = [f"Col_{i+1}" for i in range(cols)]
    writer.writerow(header)

    # Write rows
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        writer.writerow(row)

print("random_data.csv created!")