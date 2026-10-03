import csv

# Lists to store the results
processing_times = []
fps_values = []
object_counts = []

# Open the CSV file
with open("performance_results.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        processing_times.append(
            float(row["Processing_Time_ms"])
        )

        fps_values.append(
            float(row["FPS"])
        )

        object_counts.append(
            int(row["Objects"])
        )


# Calculate statistics
total_frames = len(processing_times)

minimum_time = min(processing_times)
maximum_time = max(processing_times)
average_time = sum(processing_times) / total_frames

minimum_fps = min(fps_values)
maximum_fps = max(fps_values)
average_fps = sum(fps_values) / total_frames

minimum_objects = min(object_counts)
maximum_objects = max(object_counts)
average_objects = sum(object_counts) / total_frames


# Display results
print("======================================")
print("TASK 4 FRAME-BY-FRAME EVALUATION")
print("======================================")

print()
print("Total frames:", total_frames)

print()
print("PROCESSING TIME")
print("--------------------------------------")
print("Minimum:", round(minimum_time, 2), "ms")
print("Maximum:", round(maximum_time, 2), "ms")
print("Average:", round(average_time, 2), "ms")

print()
print("FPS")
print("--------------------------------------")
print("Minimum:", round(minimum_fps, 2))
print("Maximum:", round(maximum_fps, 2))
print("Average:", round(average_fps, 2))

print()
print("OBJECT COUNT")
print("--------------------------------------")
print("Minimum:", minimum_objects)
print("Maximum:", maximum_objects)
print("Average:", round(average_objects, 2))

print()
print("======================================")
print("EVALUATION COMPLETE")
print("======================================")