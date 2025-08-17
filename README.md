# CPU Process Scheduling Algorithms with Gantt Chart Visualization

### How to Run
1. Navigate to the project folder in your terminal or command prompt.
2. Run the command: `python main.py` (PyQt5 and matplotlib modules required).
3. Enter process details in the GUI and select the desired scheduling algorithm.
4. View the generated Gantt chart and performance results.

---

### Introduction
This project is a Python-based application that implements and visualizes multiple CPU scheduling algorithms using a Gantt chart. It provides a clear and intuitive way to understand how these algorithms manage process execution.

**Supported Algorithms:**
* First-Come, First-Serve (FCFS)
* Shortest Job First (SJF) - Preemptive & Non-Preemptive
* Priority Scheduling - Preemptive & Non-Preemptive
* Round Robin (RR)

---

### Expected Output
The application generates a **Gantt chart** that visually represents the process execution order, showing each process's start time, end time, and process ID. 

---

### Requirements
#### Data Structures
* **List**: For storing process details.
* **Circular Queue**: Specifically used for the Round Robin algorithm.
* **Priority Queue**: Utilized by the SJF and Priority Scheduling algorithms to efficiently select the next process.
* **Dictionary**: Used for mapping colors to different processes for a clear visualization.

#### Software
* Python 3.13.1
* Matplotlib
* PyQt5

---

### Methodology
1. **Input**: Users can add processes by specifying their arrival time, burst time, and priority. They then select a scheduling algorithm from the available options.
2. **Execution**: The program simulates the process execution based on the chosen algorithm.
3. **Visualization**: A detailed Gantt chart is displayed, showing the sequence and timing of each process, bridging the gap between theoretical concepts and practical implementation.

---

### Project Structure

```
process_scheduler/
├── main.py
├── algorithms/
│   ├── fcfs.py
│   ├── sjf_preemptive.py
│   ├── sjf_nonpreemptive.py
│   ├── priority_preemptive.py
│   ├── priority_nonpreemptive.py
│   ├── round_robin.py
├── utils/
│   ├── process.py
│   ├── gantt_chart.py
```

---

### Conclusion

This project provides a clear simulation and visualization of CPU scheduling algorithms, including FCFS, SJF, Priority Scheduling, and Round Robin. Through a user-friendly GUI and detailed Gantt chart visualization, it bridges the gap between theory and practical implementation. It serves as an effective tool for understanding and demonstrating scheduling concepts in an intuitive and visually appealing way.
