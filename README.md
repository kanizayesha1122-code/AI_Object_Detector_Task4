# AI Object Detector & Frame-by-Frame Segmenter

A computer vision project developed as part of the **Progree AI Internship – Task 4**.

This project explores object detection and frame-by-frame video analysis using two different approaches:

1. **Classical Computer Vision with OpenCV**
2. **YOLO-based Object Detection**

The project processes video frames, detects objects/regions, records performance metrics, and generates visualizations for analysis.

---

## Project Overview

The goal of this project is to build a computer vision pipeline capable of processing video frame by frame and detecting objects using image-processing and deep-learning-based approaches.

The classical computer vision pipeline uses:

**Video → Grayscale → Gaussian Filtering → Adaptive Thresholding → Morphological Processing → Contours → Bounding Boxes**

A YOLO-based detector is also implemented to provide semantic object detection and a comparison between the two approaches.

---

## Technologies Used

- Python
- OpenCV
- YOLO (Ultralytics)
- PyTorch
- Pandas
- NumPy
- Matplotlib
- Scikit-learn compatible data-analysis workflow

---

## Project Structure

```text
AI_Object_Detector_Task4/
│
├── object_detector_classical.py
├── yolo_detector.py
│
├── analyze_results.py
├── plot_results.py
├── plot_yolo_results.py
│
├── performance_results.csv
├── yolo_performance_results.csv
│
├── processing_time_graph.png
├── yolo_processing_time_graph.png
├── yolo_fps_graph.png
├── yolo_object_count_graph.png
│
├── test.jpg
├── test.mp4
│
└── .gitignore
1. Classical OpenCV Detector

The classical detector processes each video frame using traditional image-processing techniques.

Processing Pipeline
Convert the frame to grayscale
Apply Gaussian blur
Apply adaptive thresholding
Perform morphological opening and closing
Detect contours
Filter detected regions based on size and shape
Generate bounding boxes
Count detected regions
Record processing time and FPS
Save results to CSV
Example Filtering

The detector applies constraints such as:

Minimum contour area
Width and height filtering
Aspect-ratio filtering

This helps remove some unwanted small regions from the detection results.

2. YOLO Object Detector

The project also implements object detection using YOLO11n through the Ultralytics framework.

The YOLO detector:

Processes video frames
Detects objects
Generates bounding boxes
Assigns detected object classes
Counts detected objects
Records processing time
Calculates frame processing FPS
Saves annotated video output
Saves performance data to CSV

The YOLO model file is excluded from the repository because of its size.

Performance Results

Both approaches were tested on the same 716-frame video.

Classical OpenCV
Metric	Result
Frames processed	716
Average processing time	~5.68 ms/frame
Average detected regions	~7.03/frame
Minimum processing time	4.22 ms
Maximum processing time	43.22 ms

The framewise FPS analysis produced an average of approximately 179.8 FPS.

YOLO
Metric	Result
Frames processed	716
Average processing time	~40.50 ms/frame
Average detected objects	~10.54/frame
Minimum processing time	31.14 ms
Maximum processing time	1356.17 ms
Mean framewise FPS	~26.28 FPS

The average processing time corresponds to an effective throughput of approximately 24.69 FPS when calculated as:

1000 / average_processing_time

The difference between the two FPS figures occurs because the CSV's Processing_FPS column contains a separate FPS measurement for every frame, which is then averaged.

Visualizations

The project includes graphs showing:

Classical OpenCV processing time
YOLO processing time
YOLO frame processing FPS
YOLO object count per frame

These visualizations make it possible to examine how processing cost and detected-object counts change throughout the video.

Classical Computer Vision vs YOLO

The two approaches solve the detection problem differently.

Classical OpenCV

Uses image-processing operations such as:

Thresholding
Filtering
Morphological operations
Contour detection
Shape-based filtering

Advantages:

Lightweight
Fast
Does not require a trained object-detection model
Easy to understand and modify

Limitations:

Detects regions based mainly on visual characteristics
Does not provide semantic understanding of objects
Can detect background regions as objects
Performance depends heavily on lighting, thresholding, and scene conditions
YOLO

Uses a trained deep-learning model to perform semantic object detection.

Advantages:

Detects recognized object classes
Produces bounding boxes and class predictions
More suitable for complex real-world scenes

Limitations:

Requires a trained model
More computationally expensive
Processing speed is lower than the lightweight classical pipeline on this test setup
Important Evaluation Note

The object counts from the two methods should not be interpreted as an accuracy comparison.

A complete accuracy evaluation would require ground-truth annotations for the video and metrics such as:

Precision
Recall
F1-score
mAP

This project primarily compares the processing pipeline, detected regions/objects, computational cost, and visualization results.

How to Run
Install dependencies
pip install opencv-python pandas numpy matplotlib ultralytics
Run the classical detector
python object_detector_classical.py
Analyze classical results
python analyze_results.py
Generate classical visualizations
python plot_results.py
Run YOLO detection
python yolo_detector.py
Generate YOLO visualizations
python plot_yolo_results.py
Output Files

The project generates:

CSV performance reports
Processing-time graphs
FPS graphs
Object-count graphs
Annotated detection video

The large YOLO model and generated output video are excluded using .gitignore.

Project Purpose

This project demonstrates a complete computer vision workflow, from raw video frames and image preprocessing to object detection, performance measurement, data analysis, and visualization.

It also provides practical experience with both traditional computer vision techniques and modern deep-learning-based object detection.

Internship

Program: Progree AI Internship
Task: Task 4 – Computer Vision Object Detector & Frame-by-Frame Segmenter