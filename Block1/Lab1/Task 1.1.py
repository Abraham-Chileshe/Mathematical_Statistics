import tkinter as tk
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Data: Number of members in each family
data = [
    3, 2, 5, 4, 6, 5, 3, 2, 4, 3, 4,
    2, 3, 2, 5, 2, 3, 4, 2, 5, 7, 6
]

# Step 1: Construct a discrete variational series
frequency_table = Counter(data)

# Step 2: Analyze the distribution
total_families = len(data)
unique_values = sorted(frequency_table.keys())
max_frequency = max(frequency_table.values())
mode = [value for value, frequency in frequency_table.items() if frequency == max_frequency]

# Create a Tkinter window
root = tk.Tk()
root.title("Family Size Distribution Analysis")
root.resizable(False, False)  # Make the window non-resizable

# Create frames for results and graph
results_frame = tk.Frame(root)
results_frame.grid(row=0, column=0, padx=10, pady=10)

graph_frame = tk.Frame(root)
graph_frame.grid(row=0, column=1, padx=10, pady=10)

# Display the results
discrete_variational_series_label = tk.Label(results_frame, text="Discrete Variational Series:")
discrete_variational_series_label.grid(row=0, column=0, sticky="w")

for i, value in enumerate(unique_values):
    label = tk.Label(results_frame, text=f"{value}: {frequency_table[value]} families")
    label.grid(row=i+1, column=0, sticky="w")

character_of_distribution_label = tk.Label(results_frame, text="Character of Distribution:")
character_of_distribution_label.grid(row=len(unique_values)+2, column=0, sticky="w")

total_families_label = tk.Label(results_frame, text=f"Total families: {total_families}")
total_families_label.grid(row=len(unique_values)+3, column=0, sticky="w")

mean_label = tk.Label(results_frame, text=f"Mean: {sum(data) / total_families}")
mean_label.grid(row=len(unique_values)+4, column=0, sticky="w")

mode_label = tk.Label(results_frame, text=f"Mode: {mode[0]}")
mode_label.grid(row=len(unique_values)+5, column=0, sticky="w")

median_label = tk.Label(results_frame, text=f"Median: {sorted(data)[total_families // 2]}")
median_label.grid(row=len(unique_values)+6, column=0, sticky="w")

# Plot histogram
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(frequency_table.keys(), frequency_table.values(), color='skyblue')
ax.set_xlabel('Number of Members in Family')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Family Sizes')
ax.set_xticks(range(min(data), max(data) + 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Embed the plot in Tkinter window
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the Tkinter event loop
root.mainloop()
