import time
import matplotlib.pyplot as plt
import multiprocessing

# Function to sum numbers
def sum_numbers(n):
    return sum(range(n))

# Benchmarking function for CPython performance
def benchmark_sum(n):
    start_time = time.time()  # Record the start time
    sum_numbers(n)  # Perform the summing
    return time.time() - start_time  # Return the time taken

# Parallel summing function (using multiprocessing)
def parallel_sum(start, end):
    return sum(range(start, end))

def benchmark_parallel_sum(n, num_processes=4):
    chunk_size = n // num_processes
    pool = multiprocessing.Pool(processes=num_processes)
    result = pool.starmap(parallel_sum, [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)])
    pool.close()
    pool.join()
    return sum(result)

# Main function to run benchmarking
def main():
    # Performance Benchmarking for different n values
    n_values = [1000000, 10000000, 1000000]
    times = []

    for n in n_values:
        print(f"Benchmarking sum for n = {n}...")
        time_taken = benchmark_sum(n)
        print(f"Time to sum numbers up to {n}: {time_taken} seconds")
        times.append(time_taken)

    # Plotting the performance comparison chart (CPython)
    if times:
        plt.figure(figsize=(10, 6))
        plt.plot(n_values, times, marker='o')
        plt.title("Benchmarking Sum of Numbers (CPython)")
        plt.xlabel("Value of n")
        plt.ylabel("Time (seconds)")
        plt.grid(True)
        plt.show()

    # Scalability Analysis with different numbers of processes
    process_counts = [2, 4, 8, 16]
    parallel_times = []

    print("\nStarting parallelization benchmarks...")
    for p in process_counts:
        print(f"Testing with {p} processes...")
        start_time = time.time()
        parallel_sum_time = benchmark_parallel_sum(1000000, p)
        parallel_times.append(parallel_sum_time)
        print(f"Time for {p} processes: {parallel_sum_time} seconds")

    # Ensure parallel_times has data before plotting
    if parallel_times:
        print(f"\nParallel times for different processes: {parallel_times}")
        # Plotting the scalability analysis chart (Multiprocessing)
        plt.figure(figsize=(10, 6))
        plt.plot(process_counts, parallel_times, marker='o', color='r')
        plt.title("Scalability of Parallel Sum with Different Processes")
        plt.xlabel("Number of Processes")
        plt.ylabel("Time (seconds)")
        plt.grid(True)
        plt.show()
    else:
        print("No parallel times data collected. Skipping scalability chart.")

# Ensure multiprocessing works properly on Windows
if __name__ == '__main__':
    main()
