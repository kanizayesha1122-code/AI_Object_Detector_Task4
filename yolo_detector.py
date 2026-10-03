from ultralytics import YOLO
import cv2
import csv
import time

# ==============================
# 1. Load YOLO model
# ==============================

model = YOLO("yolo11n.pt")

# ==============================
# 2. Open input video
# ==============================

input_video = "test.mp4"
output_video = "yolo_detected_output.mp4"

cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# ==============================
# 3. Get video information
# ==============================

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
original_fps = cap.get(cv2.CAP_PROP_FPS)

# ==============================
# 4. Create output video
# ==============================

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    output_video,
    fourcc,
    original_fps,
    (width, height)
)

# ==============================
# 5. Create CSV file
# ==============================

csv_file = open(
    "yolo_performance_results.csv",
    "w",
    newline=""
)

csv_writer = csv.writer(csv_file)

csv_writer.writerow([
    "Frame",
    "Object_Count",
    "Processing_Time_ms",
    "Processing_FPS"
])

# ==============================
# 6. Process every frame
# ==============================

frame_number = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    # Start timer
    start_time = time.perf_counter()

    # Run YOLO detection
    results = model(frame, verbose=False)

    # Draw bounding boxes and labels
    annotated_frame = results[0].plot()

    # Count detected objects
    object_count = len(results[0].boxes)

    # Calculate processing time
    end_time = time.perf_counter()

    processing_time = (end_time - start_time) * 1000

    # Calculate processing FPS
    processing_fps = 1000 / processing_time

    # Write results to CSV
    csv_writer.writerow([
        frame_number,
        object_count,
        round(processing_time, 2),
        round(processing_fps, 2)
    ])

    # Write frame to output video
    out.write(annotated_frame)

    # Display frame
    cv2.imshow(
        "YOLO Object Detection",
        annotated_frame
    )

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==============================
# 7. Release everything
# ==============================

cap.release()
out.release()
csv_file.close()

cv2.destroyAllWindows()

print("\n===================================")
print("YOLO VIDEO DETECTION COMPLETED")
print("===================================")
print(f"Total frames processed: {frame_number}")
print(f"Output video: {output_video}")
print("CSV results: yolo_performance_results.csv")
print("===================================")