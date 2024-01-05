from processes import Process
import numpy as np


def generator(num, arrival_min, arrival_max, burst_min, burst_max):

    processes = []
    burst_sum = 0

    for i in range(num):

        # Generating a random number from a given range
        arrival = np.random.randint(arrival_min, arrival_max + 1)
        burst = np.random.randint(burst_min, burst_max + 1)

        # Appending a list of processes with a new one
        processes.append(Process(arrival, burst))

    # Printing processes
    print('Processes:\n')
    for process in processes:
        print('Process with arrival: ', process.arrival, ' and burst: ', process.burst)
        burst_sum += process.burst
    print()

    # Returning a list of processes and average burst time
    return processes, burst_sum/len(processes)

