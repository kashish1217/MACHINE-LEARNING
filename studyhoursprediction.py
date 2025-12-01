# Very simple ML-like code in pure Python

# Training data (examples)
hours = [1, 2, 3, 4, 5]
marks = [50, 55, 65, 70, 80]

# Learn pattern: calculate average marks gained per hour
increase_per_hour = (marks[-1] - marks[0]) / (hours[-1] - hours[0])

# Let's assume marks = 45 + increase_per_hour * hours  (simple pattern)
def predict(h):
    return 45 + increase_per_hour * h

# Predict marks for 6 hours of study
print("Predicted marks for 6 hours:", predict(6))

