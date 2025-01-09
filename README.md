Process Scheduling Algorithms with Gantt Chart Visualization

How to Run
> 1. Navigate to the project folder in your terminal or command prompt.
> 2. Run the command: python main.py.
> 3. Enter process details in the GUI and select the scheduling algorithm.
> 4. View the Gantt chart and results.

Introduction
> This project implements multiple CPU scheduling algorithms with a Gantt chart visualization using Python. Algorithms include:

> First-Come-First-Serve (FCFS)
> Shortest Job First (SJF)
> Priority Scheduling (Preemptive & Non-Preemptive)
> Round Robin (RR)
> The GUI allows users to input processes and visualize their scheduling using a color-coded Gantt chart.

Expected Output
> A Gantt chart showcasing process execution order, start and end times, and process IDs, with borders for clarity.

Requirements
> Data Structures:
>   List: For process storage.
>   Queue: For Round Robin.
>   Priority Queue: For SJF and Priority Scheduling.
>   Dictionary: For color mapping.
> Software:
>   Python 3.x
>   Matplotlib
>   PyQt5

Methodology
> Input: Add processes (arrival & burst time). Select a scheduling algorithm.
> Execution: Simulates process execution.
> Visualization: Displays Gantt chart with process details.

Project Structure

> process_scheduler/
> │
> ├── main.py                    # Main entry point
> ├── algorithms/                # All scheduling algorithms
> │   ├── fcfs.py
> │   ├── sjf_preemptive.py  
> │   ├── sjf_nonpreemptive.py
> │   ├── priority_preemptive.py  
> │   ├── priority_nonpreemptive.py 
> │   ├── round_robin.py     
> │
> ├── utils/                     # Utility modules
> │   ├── process.py
> │   ├── gantt_chart.py
> │
> ├── README.md                  # Documentation

Conclusion
> This project provides a clear simulation and visualization of CPU scheduling algorithms, including FCFS, SJF, Priority Scheduling, and Round Robin. Through a user-friendly GUI and detailed Gantt chart visualization, it bridges the gap between theory and practical implementation. It serves as an effective tool for understanding and demonstrating scheduling concepts in an intuitive and visually appealing way.
