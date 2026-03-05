#A weather station recorded temperatures (in Celsius) for 5 days: 22, 25, 28, 24, 26
import numpy as np
import builtins
import time
temps_celsius=np.array([22, 25, 28, 24, 26])

#Convert all temperatures to Fahrenheit using: F = C × 1.8 + 32
temperatures_f=temps_celsius * 1.8 + 32

#Print both Celsius and Fahrenheit arrays
print(f"temperatures in Celsius:{temps_celsius}")
print(f"temperatures to Fahrenheit:{temperatures_f}")

#Calculate the average temperature in Fahrenheit
avg_temp=np.mean(temperatures_f)
print(f"Average temperature in Fahrenheit:{avg_temp:.1f}")

#Task 2: Array Shape and Statistics
test_scores=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
#Print the shape of this array
print(f"shape of the array is{test_scores.shape}")
#Find the total number of elements in the array
print(f"Total number of arrays : {len(test_scores)}")
#Calculate the highest score
Highest_score=np.max(test_scores)
print(f"Highest score:{Highest_score}")
#Calculate the lowest score
lowest_score=np.min(test_scores)
print(f"Lowest score:{lowest_score}")
#Calculate the range (difference between highest and lowest)
range=Highest_score-lowest_score
print(f"Range is:{range}")

# Task 3: Performance Comparison

# Create a NumPy array with numbers from 1 to 50000
arr_nparray = np.arange(1, 50001)
print(arr_nparray)
# Create a Python list with the same numbers
python_list = builtins.list(builtins.range(1, 50001))

print(python_list[:5])   # First 5 elements
print(python_list[-5:])  # Last 5 elements

# Calculate the sum using NumPy
start = time.perf_counter()
sum_numpy = np.sum(arr_nparray)
end = time.perf_counter()
time_numpy=(end - start)*1000


# Calculate the sum using Python list
start_lists = time.perf_counter()
sum_lists = sum(python_list)
end_lists = time.perf_counter()
time_lists=(end_lists - start_lists)*1000
#Measure and print the time taken for both operations
print(f"Sum of NumPy array: {sum_numpy}")
print(f"Time taken for NumPy: {time_numpy} ms")

print(f"Sum of Python list: {sum_lists} ms")
print(f"Time taken for list: {time_lists} ms")


#Calculate how many times faster NumPy is
speed=time_lists/time_numpy
print(f"Numpy is {speed} times faster than list")