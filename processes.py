class Process:
    def __init__(self, arrival, burst):
        self.arrival = arrival
        self.burst = burst
        self.start = 0
        self.finish = 0
        self.waiting = 0
        self.turnaround = 0

    def set_finish(self, time):
        # When setting finish, other values are also set
        self.finish = time
        self.start = self.finish - self.burst
        self.waiting = self.start - self.arrival
        self.turnaround = self.waiting + self.burst

