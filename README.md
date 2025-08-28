#  CPU SCHEDULING SIMULATOR

An interactive desktop application built with **Python** and **Tkinter** to simulate and visualize various **CPU Scheduling Algorithms**.  
This tool provides a clear comparison of algorithm performance through a dynamic **Gantt Chart** and detailed metrics like **Waiting Time** and **Turnaround Time**.

---

##  KEY FEATURES
- **MULTIPLE ALGORITHM SIMULATION** – Supports **FCFS, SJF (Preemptive & Non-preemptive), Priority (Preemptive & Non-preemptive), and Round Robin**.  
- **DYNAMIC GANTT CHART VISUALIZATION** – Generates a clear timeline of process execution.  
- **PERFORMANCE ANALYSIS** – Displays **average waiting time** and **turnaround time** automatically.  
- **INTERACTIVE GUI** – Easy-to-use interface with real-time results.  

---

##  TECHNOLOGIES USED
- **PYTHON** – Core programming language  
- **TKINTER** – For the graphical user interface (GUI)  
- **DATA STRUCTURES** – Min-heaps and queues for efficient scheduling computations  

---

##  How To Run

1. **Clone the repository:**  
   `git clone https://github.com/your-username/your-repo-name.git`

2. **Navigate to the project directory:**  
   `cd your-repo-name`

3. **Run the main application file:**  
   `python main.py`

*(Make sure you have Python installed on your system.)*

##  Usage

1. Launch the application by running the main Python script.  
2. Select a **scheduling algorithm** from the dropdown menu.  
3. Enter the **Number of Processes**.  
4. Provide the **Arrival Times** and **Burst Times** as comma-separated values.  
5. If you select a **Priority** algorithm, the **Priority input field** will appear. Enter the priorities as comma-separated values.  
6. If you select **Round Robin**, the **Time Quantum input field** will appear. Enter a single integer value.  
7. Click the **Compute** button.  
8. View the results:  
   - Detailed **process table**  
   - **Average waiting time** and **turnaround time**  
   - A **Gantt chart** drawn at the bottom of the window  

---

##  Algorithms Implemented

This simulator supports the following CPU scheduling algorithms:

- **First-Come, First-Served (FCFS)**  
- **Shortest Job First (SJF)** – Preemptive & Non-preemptive  
- **Priority Scheduling** – Preemptive & Non-preemptive  
- **Round Robin (RR)**


