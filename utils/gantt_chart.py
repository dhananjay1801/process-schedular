import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def generate_gantt_chart(schedule):
    fig, ax = plt.subplots(figsize=(12, 6))

    # for colours
    color_palette = list(mcolors.TABLEAU_COLORS.values())
    process_colors = {}  # mapping pid to a specific colour
    process_positions = {}  # mapping pid to vertical position
    y_pos = 10  # Initial vertical position
    bar_height = 5

    for pid, start, end in schedule:
        # assigning unique colour to each process
        if pid not in process_colors:
            process_colors[pid] = color_palette[(pid - 1) % len(color_palette)]

        # assigning unique vertical position to each process
        if pid not in process_positions:
            process_positions[pid] = y_pos
            y_pos += bar_height + 3  # spacing between rows

        position = process_positions[pid]
        color = process_colors[pid]

        # horizontal bar for the process with the assigned colour
        ax.broken_barh([(start, end - start)], (position, bar_height), facecolors=(color,))

        # process if label at the center of process bar
        ax.text(start + (end - start) / 2, position + bar_height / 2, f"P{pid}",
                ha="center", va="center", color="white", fontsize=10, weight="bold")

        # start time of a process bar
        ax.text(start, position + bar_height + 1, f"{start}",
                ha="center", va="center", color="black", fontsize=9)

        # end time of a process bar
        ax.text(end, position + bar_height + 1, f"{end}",
                ha="center", va="center", color="black", fontsize=9)

    # adjusting chart appearance
    ax.set_xlabel("Time")
    ax.set_yticks([pos + bar_height / 2 for pos in process_positions.values()])
    ax.set_yticklabels([f"P{pid}" for pid in process_positions.keys()])
    ax.set_title("Gantt Chart")
    ax.grid(axis="x", linestyle="--", alpha=0.7)
    ax.set_ylim(5, y_pos)
    ax.set_xlim(0, max(end for _, _, end in schedule) + 1)

    plt.tight_layout()
    plt.show()
