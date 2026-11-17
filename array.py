import sys

# Accept scores through command-line arguments
scores = list(map(int, sys.argv[1:]))

# Calculate sum and average
total = sum(scores)
average = total / len(scores)

# Find maximum and minimum
maximum = max(scores)
minimum = min(scores)

# Display results
print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
print("Maximum score:", maximum)
print("Minimum score:", minimum)