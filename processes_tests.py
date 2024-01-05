from FCFS import FCFS
from SJF import SJF
from processes_generator import generator


def printing(processes):
    print('\nAverage FCFS waiting time: ', FCFS(processes[0]))
    print('\nAverage SJF waiting time: ', SJF(processes[0]))
    print('\nAverage FCFS and SJF burst time: ', processes[1])
    return


for i in range(5):
    print('\n\nOutput nr: ', i + 1)

    # 1.1
    print("\n10 processes with arrival time 0 and burst from 1 to to 5\n")

    proc = generator(10, 0, 0, 1, 5)
    printing(proc)

    # 1.2
    print("\n50 processes with arrival time 0 and burst from 1 to to 5\n")

    proc = generator(50, 0, 0, 1, 5)
    printing(proc)

    # 1.3
    print("\n100 processes with arrival time 0 and burst from 1 to to 5\n\n")

    proc = generator(100, 0, 0, 1, 5)
    printing(proc)

    # 2.1
    print("\n10 processes with arrival time from 0 to 10 and burst 5\n")

    proc = generator(10, 0, 10, 5, 5)
    printing(proc)

    # 2.2
    print("\n50 processes with arrival time from 0 to 10 and burst 5\n")

    proc = generator(50, 0, 10, 5, 5)
    printing(proc)

    # 2.3
    print("\n100 processes with arrival time from 0 to 10 and burst 5\n\n")

    proc = generator(100, 0, 10, 5, 5)
    printing(proc)

    # 3.1
    print("\n10 processes with arrival time from 0 to 10 and burst from 1 to to 10\n")

    proc = generator(10, 0, 10, 1, 10)
    printing(proc)

    # 3.2
    print("\n50 processes with arrival time from 0 to 10 and burst from 1 to to 10\n")

    proc = generator(50, 0, 10, 1, 10)
    printing(proc)

    # 3.3
    print("\n100 processes with arrival time from 0 to 10 and burst from 1 to to 10\n\n")

    proc = generator(100, 0, 10, 1, 10)
    printing(proc)

    # 4.1
    print("\n10 processes with arrival time from 0 to 100 and burst from 1 to to 100\n")

    proc = generator(10, 0, 100, 1, 100)
    printing(proc)

    # 4.2
    print("\n50 processes with arrival time from 0 to 100 and burst from 1 to to 100\n")

    proc = generator(50, 0, 10, 1, 100)
    printing(proc)

    # 4.3
    print("\n100 processes with arrival time from 0 to 100 and burst from 1 to to 100\n")

    proc = generator(100, 0, 100, 1, 100)
    printing(proc)



