from heapq import heappush, heappop

def sjf_p_algorithm(processes, arrival_times, burst_times):
    n = len(processes)
    remaining_bt = burst_times.copy()
    completed = [False] * n
    queue = []
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_data = []

    last_process = None
    start_time = 0

    while not all(completed):
        # Add processes that arrive at current_time
        for i in range(n):
            if arrival_times[i] == current_time and not completed[i]:
                heappush(queue, (remaining_bt[i], i))

        if queue:
            burst, current_process = heappop(queue)
            if last_process != current_process:
                if last_process is not None:
                    gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})
                start_time = current_time
                last_process = current_process

            # Execute current_process for 1 time unit
            remaining_bt[current_process] -= 1
            current_time += 1

            # If still has burst time left, push back to queue
            if remaining_bt[current_process] > 0:
                heappush(queue, (remaining_bt[current_process], current_process))
            else:
                completed[current_process] = True
                turnaround_time[current_process] = current_time - arrival_times[current_process]
                waiting_time[current_process] = turnaround_time[current_process] - burst_times[current_process]
        else:
            # CPU idle
            if last_process is not None:
                gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})
                last_process = None
            current_time += 1

    # Append the last process burst to the Gantt chart
    if last_process is not None and (not gantt_data or gantt_data[-1]['end'] != current_time):
        gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})

    return waiting_time, turnaround_time, gantt_data

