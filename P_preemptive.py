import heapq

def priority_p_algorithm(processes, priority, arrival_times, burst_times):
    n = len(processes)
    remaining_bt = burst_times.copy()
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_data = []
    queue = []
    current_time = 0
    last_process = None
    start_time = 0

    while not all(completed):
        for i in range(n):
            if arrival_times[i] == current_time and not completed[i]:
                heapq.heappush(queue, (priority[i], i))

        if queue:
            curr_priority, current_process = heapq.heappop(queue)
            if last_process != current_process:
                if last_process is not None:
                    gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})
                start_time = current_time
                last_process = current_process

            remaining_bt[current_process] -= 1
            current_time += 1

            if remaining_bt[current_process] > 0:
                heapq.heappush(queue, (priority[current_process], current_process))
            else:
                completed[current_process] = True
                turnaround_time[current_process] = current_time - arrival_times[current_process]
                waiting_time[current_process] = turnaround_time[current_process] - burst_times[current_process]
        else:
            if last_process is not None:
                gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})
                last_process = None
            current_time += 1

    if last_process is not None and (not gantt_data or gantt_data[-1]['end'] != current_time):
        gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})

    return waiting_time, turnaround_time, gantt_data
