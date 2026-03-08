import matplotlib.pyplot as plt
import numpy as np

"""
This script plots the speedup of an OpenMP array sum implementation for different input sizes and thread counts.

"""

# Threads
threads = np.array([1, 2, 4, 8])

# hard coded speedup values --> openMPdata.xlsx
speedup_10k = np.array([1.00, 1.59, 2.37, 2.70])
speedup_100k = np.array([1.00, 2.38, 5.28, 7.36])
speedup_1m = np.array([1.00, 1.72, 3.10, 3.04])
speedup_10m = np.array([1.00, 1.84, 3.24, 3.60])

plt.figure(figsize=(8,5))

# Ideal speedup line
plt.plot(threads, threads, '--', label="Ideal Speedup")

# Measured results
plt.plot(threads, speedup_10k, marker='o', label="10k")
plt.plot(threads, speedup_100k, marker='o', label="100k")
plt.plot(threads, speedup_1m, marker='o', label="1m")
plt.plot(threads, speedup_10m, marker='o', label="10m")

plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("OpenMP Array Sum Speedup")
plt.grid(True)
plt.legend()

# Save figure
plt.savefig("speedup_plot.png", dpi=300)

print("Plot saved as speedup_plot.png")
