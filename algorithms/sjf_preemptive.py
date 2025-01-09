def sjf_preemptive(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    completed = 0
    n = len(processes)
    schedule = []

    while completed < n:
        available = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]
        if available:
            current_process = min(available, key=lambda x: x.remaining_time)
            start_time = current_time
            current_time += 1
            current_process.remaining_time -= 1
            if current_process.remaining_time == 0:
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed += 1
            schedule.append((current_process.pid, start_time, current_time))
        else:
            current_time += 1

    return processes, schedule