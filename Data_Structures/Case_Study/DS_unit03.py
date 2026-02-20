from collections import deque

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def round_robin_scheduling(process_list, time_quantum):
    queue = deque(process_list)
    time = 0
    execution_order = []

    while queue:
        process = queue.popleft()

        # If remaining time > time quantum, execute for time quantum
        if process.remaining_time > time_quantum:
            time += time_quantum
            process.remaining_time -= time_quantum
            execution_order.append((process.pid, time))
            # new process can enter dynamically (simulation)
            queue.append(process)
        else:
            # Process completes execution
            time += process.remaining_time
            process.remaining_time = 0
            process.turnaround_time = time
            process.waiting_time = process.turnaround_time - process.burst_time
            execution_order.append((process.pid, time))
    
    # Display result
    print("\n--- Round Robin Scheduling Simulation ---")
    print("Process\tBurst\tWaiting\tTurnaround")
    total_wt = total_tat = 0
    for p in process_list:
        total_wt += p.waiting_time
        total_tat += p.turnaround_time
        print(f"{p.pid}\t{p.burst_time}\t{p.waiting_time}\t{p.turnaround_time}")

    print("\nAverage Waiting Time:", round(total_wt / len(process_list), 2))
    print("Average Turnaround Time:", round(total_tat / len(process_list), 2))
    print("\nExecution Order (PID, Time):", execution_order)


# ---------- Example Input ----------
if __name__ == "__main__":
    # Create initial processes
    process_list = [
        Process("P1", 5),
        Process("P2", 4),
        Process("P3", 6)
    ]

    time_quantum = 2  # Equal time slice for each process

    # Run the scheduler
    round_robin_scheduling(process_list, time_quantum)
