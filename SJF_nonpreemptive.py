from heapq import heappush, heappop

def sjf_np_algorithm(processes, arrival_times, burst_times):
    n = len(processes)
    completed = [False] * n
    queue = []
    current_time = 0
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_data = []

    while not all(completed):
        for i in range(n):
            if arrival_times[i] == current_time and not completed[i] and i not in [idx for _, idx in queue]:
                heappush(queue, (burst_times[i], i))
        if queue:
            burst, current_process = heappop(queue)
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
                    i not in [idx for _, idx in queue]):
                    heappush(queue, (burst_times[i], i))
        else:
            current_time += 1

    return waiting_time, turnaround_time, gantt_data

p=[0,1,2,3]
wt=[]