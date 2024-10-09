import pandas as pd
import numpy as np
from scipy import stats

# Creating a DataFrame from the given grades
data = {
    'Name': ['Adam', 'Anna', 'James', 'Corey', 'Alisha', 'Jodie', 'John'],
    'Math': [11, 12, 11, 7, 9.5, 15, 18],
    'Science': [9, 11, 18, 15.5, 12, 18.5, 15.5],
    'Reading': [16, 8.5, 11.5, 11, 10.5, 7, 11],
    'History': [13.5, 10, 9, 14, 14, 12, 7.5]
}

df = pd.DataFrame(data)

# Calculate mean for each subject
mean_grades = df[['Math', 'Science', 'Reading', 'History']].mean()
print("Mean Grades:")
print(mean_grades)

# Find median grade in Math
median_math = df['Math'].median()
print("\nMedian Math Grade:", median_math)

# Calculate mode for History
mode_history = stats.mode(df['History']).mode[0]
print("\nMode History Grade:", mode_history)

# Calculate the correlation between subjects
correlation = df[['Math', 'Science', 'Reading', 'History']].corr()
print("\nCorrelation Matrix:")
print(correlation)

# Find the strongest correlation
strongest_correlation = correlation.unstack().sort_values(ascending=False)
# Exclude self-correlation
strongest_correlation = strongest_correlation[strongest_correlation < 1]
strongest_pair = strongest_correlation.idxmax()
strongest_value = strongest_correlation.max()

print("\nStrongest Correlation between Subjects:")
print(f"{strongest_pair[0]} and {strongest_pair[1]} with a correlation of {strongest_value:.2f}")


def desc_stats(scores):
    mean = np.mean(scores)
    median = np.median(scores)
    mode = stats.mode(scores).mode[0]
    minimum = np.min(scores)
    maximum = np.max(scores)
    range_ = maximum - minimum
    variance = np.var(scores, ddof=0)  # Population variance
    std_dev = np.std(scores, ddof=0)  # Population standard deviation

    print("Statistical Calculations:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Range: {range_}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")


# List of exam scores
exam_scores = [24, 5, 15, 60, 54, 82, 99, 80, 70, 98, 93, 60, 33, 22, 65, 61, 51, 58, 83, 86, 42, 67, 60]

# Call the function to print the results
desc_stats(exam_scores)
