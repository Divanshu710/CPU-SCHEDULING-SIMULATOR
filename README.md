CPU Scheduling Simulator
An interactive desktop application built with Python and Tkinter to simulate and visualize various CPU scheduling algorithms. This tool provides a clear comparison of algorithm performance through a dynamic Gantt chart and detailed metrics like waiting time and turnaround time.

Replace the placeholder above with a screenshot of your application.

 Key Features
Multiple Algorithm Simulation: Simulates FCFS, SJF (preemptive and non-preemptive), Priority (preemptive and non-preemptive), and Round Robin.

Dynamic Gantt Chart Visualization: Generates a clear Gantt chart to visualize the execution timeline for each algorithm.

Performance Analysis: Automatically calculates and displays key performance metrics, including average waiting time and turnaround time.

Interactive GUI: A user-friendly interface for easy input of process data and immediate visualization of results.

 Technologies Used
Python: Core programming language.

Tkinter: For the graphical user interface (GUI).

Data Structures: Min-heaps and queues for efficient scheduling computations.

 How To Run
Clone the repository:

git clone https://github.com/your-username/your-repo-name.git

Navigate to the project directory:

cd your-repo-name

Run the main application file:

python main.py 

(Make sure you have Python installed on your system.)

Usage
Launch the application by running the main Python script.

Select a scheduling algorithm from the dropdown menu.

Enter the Number of Processes.

Provide the Arrival Times and Burst Times as comma-separated values.

If you select a "Priority" algorithm, the Priority input field will appear. Enter the priorities as comma-separated values.

If you select "Round Robin", the Time Quantum input field will appear. Enter a single integer value.

Click the "Compute" button.

The results, including a detailed process table and average times, will be displayed in the output box.

The corresponding Gantt chart will be drawn at the bottom of the window.

 Algorithms Implemented
This simulator supports the following CPU scheduling algorithms:

First-Come, First-Served (FCFS)

Shortest Job First (SJF) (Preemptive and Non-preemptive)

Priority Scheduling (Preemptive and Non-preemptive)

Round Robin

