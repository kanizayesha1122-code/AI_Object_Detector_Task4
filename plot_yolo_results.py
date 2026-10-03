import pandas as pd
import matplotlib.pyplot as plt

# Load YOLO performance results
df = pd.read_csv("yolo_performance_results.csv")

# -----------------------------------
# Graph 1: Processing Time
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Frame"],
    df["Processing_Time_ms"]
)

plt.xlabel("Frame Number")
plt.ylabel("Processing Time (ms)")
plt.title("YOLO Processing Time per Frame")
plt.grid(True)

plt.savefig("yolo_processing_time_graph.png")
plt.show()


# -----------------------------------
# Graph 2: Processing FPS
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Frame"],
    df["Processing_FPS"]
)

plt.xlabel("Frame Number")
plt.ylabel("Processing FPS")
plt.title("YOLO Processing FPS per Frame")
plt.grid(True)

plt.savefig("yolo_fps_graph.png")
plt.show()


# -----------------------------------
# Graph 3: Object Count
# -----------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df["Frame"],
    df["Object_Count"]
)

plt.xlabel("Frame Number")
plt.ylabel("Number of Detected Objects")
plt.title("YOLO Detected Objects per Frame")
plt.grid(True)

plt.savefig("yolo_object_count_graph.png")
plt.show()


# -----------------------------------
# Print summary
# -----------------------------------

print("\n===================================")
print("YOLO GRAPH ANALYSIS")
print("===================================")

print(f"Total frames: {len(df)}")
print(f"Average objects/frame: {df['Object_Count'].mean():.2f}")
print(f"Average processing time: {df['Processing_Time_ms'].mean():.2f} ms")
print(f"Average FPS: {df['Processing_FPS'].mean():.2f}")

print("\nGraphs saved:")
print("1. yolo_processing_time_graph.png")
print("2. yolo_fps_graph.png")
print("3. yolo_object_count_graph.png")

print("===================================")