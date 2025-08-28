import tkinter as tk
from tkinter import messagebox, ttk
from FCFS import fcfsalgorithm
from SJF_nonpreemptive import sjf_np_algorithm
from SJF_preemptive import sjf_p_algorithm
from P_nonpreemptive import priority_np_heap
from P_preemptive import priority_p_algorithm
from Round_robin import round_robin_algorithm
from gantt_drawer import draw_gantt_chart

def clear_inputs():
    for widget in (priority_frame, quantum_frame):
        for child in widget.winfo_children():
            child.grid_forget()
        widget.place_forget()

def on_algo_change(event=None):
    clear_inputs()
    algo = algo_var.get()
    if algo.startswith("Priority"):
        priority_frame.place(x=370, y=110)
        tk.Label(priority_frame, text="Priority (comma separated):", anchor='w').grid(row=0, column=0, sticky="w")
        priority_entry.grid(row=0, column=1, padx=10)
    if algo == "Round Robin":
        quantum_frame.place(x=370, y=140)
        tk.Label(quantum_frame, text="Time Quantum:", anchor='w').grid(row=0, column=0, sticky="w")
        quantum_entry.grid(row=0, column=1, padx=10)

def on_run():
    try:
        algo = algo_var.get()
        num = int(num_entry.get())
        processes = list(range(num))
        arrival = list(map(int, arrival_entry.get().split(',')))
        burst = list(map(int, burst_entry.get().split(',')))
        if len(arrival) != num or len(burst) != num:
            messagebox.showerror("Input Error", "Number of entries must match Number of Processes.")
            return

        priority = None
        quantum = None
        if algo.startswith("Priority"):
            priority = list(map(int, priority_entry.get().split(',')))
            if len(priority) != num:
                messagebox.showerror("Input Error", "Number of priorities must match Number of Processes.")
                return
        if algo == "Round Robin":
            quantum = int(quantum_entry.get())
            if quantum <= 0:
                messagebox.showerror("Input Error", "Quantum must be a positive integer.")
                return

        if algo == "FCFS":
            wt, tat, gantt_data = fcfsalgorithm(processes, arrival, burst)
        elif algo == "SJF (Non-preemptive)":
            wt, tat, gantt_data = sjf_np_algorithm(processes, arrival, burst)
        elif algo == "SJF (Preemptive)":
            wt, tat, gantt_data = sjf_p_algorithm(processes, arrival, burst)
        elif algo == "Priority (Non-preemptive)":
            wt, tat, gantt_data = priority_np_heap(processes, priority, arrival, burst)
        elif algo == "Priority (Preemptive)":
            wt, tat, gantt_data = priority_p_algorithm(processes, priority, arrival, burst)
        elif algo == "Round Robin":
            wt, tat, gantt_data = round_robin_algorithm(processes, arrival, burst, quantum)
        else:
            messagebox.showerror("Error", "Select an algorithm.")
            return

        result = "Process | Arrival | Burst"
        if priority is not None:
            result += " | Priority"
        result += " | Waiting | Turnaround\n" + "-"*60 + "\n"
        for p in range(num):
            row = f"{p+1:^7} | {arrival[p]:^7} | {burst[p]:^5}"
            if priority is not None:
                row += f" | {priority[p]:^8}"
            row += f" | {wt[p]:^7} | {tat[p]:^10}\n"
            result += row
        result += f"\nAverage Waiting Time: {sum(wt)/num:.2f}\n"
        result += f"Average Turnaround Time: {sum(tat)/num:.2f}"
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state="disabled")
        canvas.delete("all")
        draw_gantt_chart(canvas, gantt_data)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("CPU Scheduling Simulator")
root.geometry("900x700")
root.resizable(False, False)
root.configure(bg="#f6f6f6")

# Top Algorithm selector
tk.Label(root, text="Algorithm:", font=("Segoe UI", 11), bg="#f6f6f6").place(x=340, y=30)
algo_var = tk.StringVar()
ALGO_OPTIONS = [
    "FCFS",
    "SJF (Non-preemptive)",
    "SJF (Preemptive)",
    "Priority (Non-preemptive)",
    "Priority (Preemptive)",
    "Round Robin"
]
algo_menu = ttk.Combobox(root, textvariable=algo_var, values=ALGO_OPTIONS, state="readonly", width=25, font=("Segoe UI", 11))
algo_menu.set(ALGO_OPTIONS[0])
algo_menu.place(x=420, y=30)
algo_menu.bind('<<ComboboxSelected>>', on_algo_change)

# Input fields
input_frame = tk.Frame(root, bg="#f6f6f6")
input_frame.place(x=160, y=70)
tk.Label(input_frame, text="Number of Processes:", bg="#f6f6f6").grid(row=0, column=0, sticky="w")
num_entry = tk.Entry(input_frame, width=10)
num_entry.grid(row=0, column=1, padx=6)
tk.Label(input_frame, text="Arrival Times (comma separated):", bg="#f6f6f6").grid(row=1, column=0, sticky="w")
arrival_entry = tk.Entry(input_frame, width=25)
arrival_entry.grid(row=1, column=1, padx=6)
tk.Label(input_frame, text="Burst Times (comma separated):", bg="#f6f6f6").grid(row=2, column=0, sticky="w")
burst_entry = tk.Entry(input_frame, width=25)
burst_entry.grid(row=2, column=1, padx=6)

# Priority and Quantum fields (shown only if needed)
priority_frame = tk.Frame(root, bg="#f6f6f6")
priority_entry = tk.Entry(priority_frame, width=25)
quantum_frame = tk.Frame(root, bg="#f6f6f6")
quantum_entry = tk.Entry(quantum_frame, width=10)

# Compute Button
compute_btn = tk.Button(root, text="Compute", bg="#4287f5", fg="white", font=("Segoe UI", 12, "bold"),
                        width=18, height=2, command=on_run, relief='raised', bd=3, activebackground="#6595ec")
compute_btn.place(x=390, y=170)

# Output Text Box
output_text = tk.Text(root, width=100, height=12, state="disabled", font=("Consolas", 12),
                      bg="white", fg="black", wrap="none", bd=2, relief="groove")
output_text.place(x=40, y=240)

# Gantt Chart Canvas
canvas = tk.Canvas(root, bg='white', height=130, bd=2, relief="groove")
canvas.place(x=40, y=450, width=820)


on_algo_change()  # Ensure correct fields are visible for default selection
root.mainloop()
