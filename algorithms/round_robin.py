def round_robin(processes, time_quantum):
    processes.sort(key=lambda x: x.arrival_time)
    queue = []
    current_time = 0
    schedule = []

    for process in processes:
        process.remaining_time = process.burst_time

    while any(p.remaining_time > 0 for p in processes):
        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0 and process not in queue:
                queue.append(process)

        if queue:
            current_process = queue.pop(0)
            start_time = current_time
            execution_time = min(current_process.remaining_time, time_quantum)
            current_time += execution_time
            current_process.remaining_time -= execution_time
            schedule.append((current_process.pid, start_time, current_time))

            if current_process.remaining_time > 0:
                queue.append(current_process)
            else:
                current_process.completion_time = current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        else:
            current_time += 1

    return processes, schedule
