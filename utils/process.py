class Process:
    pid_counter = 1  # to auto assign pids

    def __init__(self, arrival_time, burst_time, priority=None):
        self.pid = Process.pid_counter
        Process.pid_counter += 1
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

    @staticmethod
    def reset_pid_counter():
        Process.pid_counter = 1  # resets counter for new process sets
