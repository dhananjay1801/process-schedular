def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    schedule = []

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        start_time = current_time
        current_time += process.burst_time
        end_time = current_time

        process.completion_time = end_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

        schedule.append((process.pid, start_time, end_time))

    return processes, schedule
