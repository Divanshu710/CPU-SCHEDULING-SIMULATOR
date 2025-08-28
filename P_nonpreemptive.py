import heapq

def priority_np_heap(processes, priority, arrival_times, burst_times):
    n = len(processes)
    completed = [False] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_data = []
    queue = []
    current_time = 0

    while not all(completed):
        for i in range(n):
            if arrival_times[i] <= current_time and not completed[i] and i not in [idx for _, idx in queue]:
                heapq.heappush(queue, (priority[i], i))

        if queue:
            curr_priority, current_process = heapq.heappop(queue)
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

            # Remove any processes that were completed while they were still in the heap
            queue = [(p, idx) for (p, idx) in queue if not completed[idx]]
            heapq.heapify(queue)
        else:
            current_time += 1

    return waiting_time, turnaround_time, gantt_data
