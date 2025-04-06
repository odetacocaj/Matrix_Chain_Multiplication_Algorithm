import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matrix_chain import compute_matrix_chain  # your function here

# Function to test for different matrix sizes
def test_matrix_chain(num_matrices):
    # Generate random matrix dimensions (num_matrices + 1 dimensions)
    dimensions = [random.randint(10, 100) for _ in range(num_matrices + 1)]
    
    start = time.perf_counter()  # Start time measurement
    compute_matrix_chain(dimensions)
    end = time.perf_counter()  # End time measurement
    
    return end - start

# Matrix counts to test
matrix_counts = [i for i in range(10, 101, 10)]  # Test from 10 to 100 matrices

# Store execution times for each matrix count
execution_times = []

# Test each matrix count and repeat multiple times (e.g., 5 times) to average the results
for count in matrix_counts:
    total_time = 0
    for _ in range(5):  # Repeat 5 times
        total_time += test_matrix_chain(count)
    execution_times.append(total_time / 5)  # Average time over 5 tests

# Plot the results to visualize the time complexity
matrix_counts = np.array(matrix_counts)
execution_times = np.array(execution_times)

# Fit a cubic curve (polynomial of degree 3) to the data
coeffs = np.polyfit(matrix_counts, execution_times, 3)
poly = np.poly1d(coeffs)

# Generate fitted values for the cubic curve
fit_values = poly(matrix_counts)

# Plot the measured times and cubic fit
plt.figure(figsize=(8, 5))
plt.plot(matrix_counts, execution_times, label="Measured times", marker='o', color='blue')
plt.plot(matrix_counts, fit_values, label="Cubic fit (O(n^3))", color='red', linestyle='--')
plt.title("Matrix Chain Multiplication - Time Complexity (Empirical)")
plt.xlabel("Number of Matrices")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
