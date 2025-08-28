def fcfsalgorithm(processes, arrival_times, burst_times):
    n = len(processes)
    completed = [False] * n
    queue = []
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_data = []

    while not all(completed):
        for i in range(n):
            if arrival_times[i] == current_time and not completed[i] and i not in queue:
                queue.append(i)
        if queue:
            current_process = queue.pop(0)
            start_time = current_time
            current_time += burst_times[current_process]
            end_time = current_time
            turnaround_time[current_process] = end_time - arrival_times[current_process]
            waiting_time[current_process] = turnaround_time[current_process] - burst_times[current_process]
            completed[current_process] = True
            gantt_data.append({
                'process': f'P{processes[current_process]}',
                'start': start_time,
                'end': end_time
            })
            for i in range(n):
                if (arrival_times[i] > arrival_times[current_process] and
                    arrival_times[i] <= current_time and
                    not completed[i] and
                    i not in queue):
                    queue.append(i)
        else:
            current_time += 1
    return waiting_time, turnaround_time, gantt_data
