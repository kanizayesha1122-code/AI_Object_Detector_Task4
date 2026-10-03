import csv
import matplotlib.pyplot as plt

# Lists for storing CSV data
frames = []
processing_times = []
fps_values = []

# Read the CSV file
with open("performance_results.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        frames.append(
            int(row["Frame"])
        )

        processing_times.append(
            float(row["Processing_Time_ms"])
        )

        fps_values.append(
            float(row["FPS"])
        )


# ==========================================
# GRAPH 1: PROCESSING TIME
# ==========================================

plt.figure()

plt.plot(
    frames,
    processing_times
)

plt.title("Frame-by-Frame Processing Time")
plt.xlabel("Frame Number")
plt.ylabel("Processing Time (ms)")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "processing_time_graph.png"
)

plt.show()


# ==========================================
# GRAPH 2: FPS
# ==========================================

plt.figure()

plt.plot(
    frames,
    fps_values
)

plt.title("Frame-by-Frame Processing FPS")
plt.xlabel("Frame Number")
plt.ylabel("FPS")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "fps_graph.png"
)

plt.show()


print("======================================")
print("GRAPHS CREATED SUCCESSFULLY")
print("======================================")
print("Saved:")
print("processing_time_graph.png")
print("fps_graph.png")