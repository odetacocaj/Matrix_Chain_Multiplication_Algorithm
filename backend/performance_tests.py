import time
import random
import psutil  
import numpy as np
from matrix_chain import compute_matrix_chain  

def test_matrix_chain(num_matrices):
    # Generate random matrix dimensions (num_matrices + 1 dimensions)
    dimensions = [random.randint(10, 100) for _ in range(num_matrices + 1)]
    
    # Start measuring memory and time
    process = psutil.Process()  # Get current process
    start_time = time.perf_counter()  # Start time measurement
    start_memory = process.memory_info().rss / (1024 * 1024)  # Start memory usage in MB
    
    compute_matrix_chain(dimensions)  # Run the algorithm
    
    end_time = time.perf_counter()  # End time measurement
    end_memory = process.memory_info().rss / (1024 * 1024)  # End memory usage in MB
    
    time_taken = end_time - start_time  # Execution time in seconds
    memory_used = end_memory - start_memory  # Memory used in MB
    
    return time_taken, memory_used

# Matrix counts to test
matrix_counts = [i for i in range(10, 101, 10)]  # Test from 10 to 100 matrices

# Store execution times and memory usage for each matrix count
execution_times = []
memory_usages = []

for count in matrix_counts:
    total_time = 0
    total_memory = 0
    for _ in range(5): 
        time_taken, memory_used = test_matrix_chain(count)
        total_time += time_taken
        total_memory += memory_used
    execution_times.append(total_time / 5) 
    memory_usages.append(total_memory / 5)  

# Print the results in a tabular format
print("Matrix Count | Avg Execution Time (s) | Avg Memory Usage (MB)")
print("------------------------------------------------------------")
for i in range(len(matrix_counts)):
    print(f"{matrix_counts[i]:<13} | {execution_times[i]:<22} | {memory_usages[i]:<18}")
