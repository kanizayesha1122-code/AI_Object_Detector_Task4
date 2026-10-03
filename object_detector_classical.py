import cv2
import time
import csv

# Open the video
video = cv2.VideoCapture("test.mp4")

# Frame counter
frame_number = 0

# Minimum contour area
MIN_AREA = 500

# Performance statistics
total_processing_time = 0

# Create CSV file
csv_file = open(
    "performance_results.csv",
    "w",
    newline=""
)

csv_writer = csv.writer(csv_file)

# Write CSV header
csv_writer.writerow([
    "Frame",
    "Objects",
    "Processing_Time_ms",
    "FPS"
])

# Create morphological kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (5, 5)
)

while True:

    # Read one frame
    success, frame = video.read()

    # Stop when video ends
    if not success:
        break

    # Count the frame
    frame_number += 1

    # Start timer
    start_time = time.perf_counter()

    # Convert to grayscale
    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    # Apply Gaussian blur
    blurred_frame = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Apply adaptive thresholding
    thresholded_frame = cv2.adaptiveThreshold(
        blurred_frame,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Morphological opening
    opened_frame = cv2.morphologyEx(
        thresholded_frame,
        cv2.MORPH_OPEN,
        kernel
    )

    # Morphological closing
    cleaned_frame = cv2.morphologyEx(
        opened_frame,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Find contours
    contours, hierarchy = cv2.findContours(
        cleaned_frame,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Copy frame for drawing
    detection_frame = frame.copy()

    # Count detected objects
    object_count = 0

    # Process contours
    for contour in contours:

        # Calculate contour area
        area = cv2.contourArea(contour)

        # Ignore small regions
        if area < MIN_AREA:
            continue

        # Find bounding box
        x, y, width, height = cv2.boundingRect(
            contour
        )

        # Avoid extremely thin or small regions
        if width < 20 or height < 20:
            continue

        # Calculate aspect ratio
        aspect_ratio = width / height

        # Reject extremely wide or tall regions
        if aspect_ratio < 0.3 or aspect_ratio > 4.0:
            continue

        # Count detected region
        object_count += 1

        # Draw bounding box
        cv2.rectangle(
            detection_frame,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )

        # Label object
        cv2.putText(
            detection_frame,
            f"Object {object_count}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # Stop timer
    end_time = time.perf_counter()

    # Calculate processing time
    processing_time = end_time - start_time

    # Add to total processing time
    total_processing_time += processing_time

    # Calculate FPS
    fps = (
        1 / processing_time
        if processing_time > 0
        else 0
    )

    # Save frame data to CSV
    csv_writer.writerow([
        frame_number,
        object_count,
        round(processing_time * 1000, 2),
        round(fps, 2)
    ])

    # Display frame number
    cv2.putText(
        detection_frame,
        f"Frame: {frame_number}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    # Display object count
    cv2.putText(
        detection_frame,
        f"Objects: {object_count}",
        (20, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    # Display processing time
    cv2.putText(
        detection_frame,
        f"Processing: {processing_time * 1000:.2f} ms",
        (20, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    # Display FPS
    cv2.putText(
        detection_frame,
        f"FPS: {fps:.2f}",
        (20, 125),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    # Show detection result
    cv2.imshow(
        "Task 4 - Object Detection",
        detection_frame
    )

    # Press Q to stop
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Release video
video.release()

# Close CSV file
csv_file.close()

# Close OpenCV windows
cv2.destroyAllWindows()

# Calculate average processing time
if frame_number > 0:

    average_time = (
        total_processing_time / frame_number
    )

    print("===================================")
    print("TASK 4 PERFORMANCE RESULTS")
    print("===================================")

    print(
        "Total frames processed:",
        frame_number
    )

    print(
        "Average processing time:",
        round(average_time * 1000, 2),
        "ms"
    )

    print(
        "Average processing FPS:",
        round(1 / average_time, 2)
    )

    print(
        "Performance data saved to:",
        "performance_results.csv"
    )