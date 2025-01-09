import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QPushButton, QWidget, QComboBox, QLineEdit, QMessageBox
)
from algorithms.fcfs import fcfs
from algorithms.sjf_preemptive import sjf_preemptive
from algorithms.sjf_nonpreemptive import sjf_nonpreemptive
from algorithms.priority_preemptive import priority_preemptive
from algorithms.priority_nonpreemptive import priority_nonpreemptive
from algorithms.round_robin import round_robin
from utils.process import Process
from utils.gantt_chart import generate_gantt_chart


class SchedulerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process Scheduler")
        self.setGeometry(100, 100, 800, 600)

        self.processes = []

        # main layout
        main_layout = QVBoxLayout()

        # input table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Arrival Time", "Burst Time", "Priority"])
        main_layout.addWidget(self.table)

        # add and remove process
        button_layout = QHBoxLayout()
        self.add_btn = QPushButton("Add Process")
        self.add_btn.clicked.connect(self.add_process)
        button_layout.addWidget(self.add_btn)

        self.remove_btn = QPushButton("Remove Selected")
        self.remove_btn.clicked.connect(self.remove_process)
        button_layout.addWidget(self.remove_btn)

        main_layout.addLayout(button_layout)

        # select algorithm
        algo_layout = QHBoxLayout()
        self.algo_combo = QComboBox()
        self.algo_combo.addItems([
            "FCFS", "SJF (Preemptive)", "SJF (Non-Preemptive)",
            "Priority (Preemptive)", "Priority (Non-Preemptive)", "Round Robin"
        ])
        algo_layout.addWidget(QLabel("Select Algorithm:"))
        algo_layout.addWidget(self.algo_combo)

        self.time_quantum_input = QLineEdit()
        self.time_quantum_input.setPlaceholderText("Time Quantum (for Round Robin)")
        algo_layout.addWidget(self.time_quantum_input)

        self.run_btn = QPushButton("Run Scheduler")
        self.run_btn.clicked.connect(self.run_scheduler)
        algo_layout.addWidget(self.run_btn)

        main_layout.addLayout(algo_layout)

        # table for results
        self.result_table = QTableWidget(0, 6)
        self.result_table.setHorizontalHeaderLabels(
            ["PID", "Arrival", "Burst", "Completion", "Waiting", "Turnaround"]
        )
        main_layout.addWidget(self.result_table)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def add_process(self):
        self.table.insertRow(self.table.rowCount())

    def remove_process(self):
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)

    def run_scheduler(self):
        self.processes = []
        for row in range(self.table.rowCount()):
            arrival_time = self.table.item(row, 0)
            burst_time = self.table.item(row, 1)
            priority = self.table.item(row, 2)

            if arrival_time and burst_time:
                try:
                    process = Process(
                        int(arrival_time.text()),
                        int(burst_time.text()),
                        int(priority.text()) if priority else None,
                    )
                    self.processes.append(process)
                except ValueError:
                    QMessageBox.warning(self, "Error", f"Invalid input at row {row + 1}.")
                    return

        algo = self.algo_combo.currentText()
        schedule = []
        if algo == "FCFS":
            results, schedule = fcfs(self.processes)
        elif algo == "SJF (Preemptive)":
            results, schedule = sjf_preemptive(self.processes)
        elif algo == "SJF (Non-Preemptive)":
            results, schedule = sjf_nonpreemptive(self.processes)
        elif algo == "Priority (Preemptive)":
            results, schedule = priority_preemptive(self.processes)
        elif algo == "Priority (Non-Preemptive)":
            results, schedule = priority_nonpreemptive(self.processes)
        elif algo == "Round Robin":
            try:
                time_quantum = int(self.time_quantum_input.text())
                results, schedule = round_robin(self.processes, time_quantum)
            except ValueError:
                QMessageBox.warning(self, "Error", "Invalid time quantum for Round Robin.")
                return

        self.display_results(results)
        generate_gantt_chart(schedule)

    def display_results(self, results):
        self.result_table.setRowCount(len(results))
        for row, process in enumerate(results):
            self.result_table.setItem(row, 0, QTableWidgetItem(str(process.pid)))
            self.result_table.setItem(row, 1, QTableWidgetItem(str(process.arrival_time)))
            self.result_table.setItem(row, 2, QTableWidgetItem(str(process.burst_time)))
            self.result_table.setItem(row, 3, QTableWidgetItem(str(process.completion_time)))
            self.result_table.setItem(row, 4, QTableWidgetItem(str(process.waiting_time)))
            self.result_table.setItem(row, 5, QTableWidgetItem(str(process.turnaround_time)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SchedulerGUI()
    window.show()
    sys.exit(app.exec_())