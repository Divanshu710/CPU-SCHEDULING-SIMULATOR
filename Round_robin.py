from collections import deque

def round_robin_algorithm(processes, arrival_times, burst_times, time_quantum):
    n = len(processes)
    remaining_bt = burst_times.copy()
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_data = []
    queue = deque()
    current_time = 0
    last_process = None
    start_time = 0

    added = [False] * n

    while not all(completed):
        # Add newly arrived processes
        for i in range(n):
            if arrival_times[i] <= current_time and not added[i] and not completed[i]:
                queue.append(i)
                added[i] = True

        if queue:
            current_process = queue.popleft()

            if last_process != current_process:
                if last_process is not None:
                    gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})
                start_time = current_time
                last_process = current_process

            execute_time = min(time_quantum, remaining_bt[current_process])
            remaining_bt[current_process] -= execute_time
            current_time += execute_time

            # Add any processes that arrived during this execution window
            for i in range(n):
                if arrival_times[i] <= current_time and not added[i] and not completed[i]:
                    queue.append(i)
                    added[i] = True

            if remaining_bt[current_process] > 0:
                queue.append(current_process)
            else:
                completed[current_process] = True
                turnaround_time[current_process] = current_time - arrival_times[current_process]
                waiting_time[current_process] = turnaround_time[current_process] - burst_times[current_process]
        else:
            # CPU idle (no process in queue)
            if last_process is not None:
                gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})
                last_process = None
            current_time += 1

    if last_process is not None and (not gantt_data or gantt_data[-1]['end'] != current_time):
        gantt_data.append({'process': f'P{last_process}', 'start': start_time, 'end': current_time})

    return waiting_time, turnaround_time, gantt_data
