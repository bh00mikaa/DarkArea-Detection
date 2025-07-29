# Real-time Dark Spot Detection


This project implements a basic real-time dark spot detection system using your laptop's camera. It's built with Python and OpenCV, offering a simple yet functional approach to identify dark regions in a live video stream.

## ✨ Features

* **Real-time Processing:** Analyzes live video stream directly from your laptop camera.
* **Fundamental Image Processing:**
    * **Grayscale Conversion:** Processes images in a single channel for efficiency.
    * **Histogram Equalization:** Enhances overall image contrast.
    * **Gaussian Blurring:** Reduces general noise in the image.
    * **Fixed Thresholding:** Segments dark areas based on a predefined intensity level.
* **Contour-Based Detection:** Identifies potential dark spots by analyzing connected regions.
* **Basic Contour Filtering:** Filters contours based on a minimum area to avoid very small noise detections.
* **Bounding Box Visualization:** Draws green rectangles around detected dark spots.
* **Spot Count Overlay:** Displays the total number of detected dark spots on the screen.
* **Toggleable Threshold View:** Switch between the processed output and the binary threshold image for inspection.
* **Frame Saving:** Save the current processed frame to an image file.
* **Simplified Camera Initialization:** Directly attempts to open camera index 0 (or a specified index) for quick setup.

## 🚀 How it Works

The detection pipeline for each frame involves the following steps:

1.  **Grayscale Conversion:** The input color frame is converted to grayscale.
2.  **Histogram Equalization:** The contrast of the grayscale image is enhanced globally.
3.  **Gaussian Blurring:** The image is smoothed to reduce high-frequency noise.
4.  **Fixed Thresholding:** A binary image is created by setting pixels below a certain intensity threshold to white (representing dark spots) and others to black.
5.  **Contour Detection:** Contours (outlines of connected white pixels) are found in the thresholded image.
6.  **Contour Filtering:** Each detected contour is checked to ensure its area is above a minimum size.
7.  **Visualization:** Bounding boxes are drawn around the filtered contours, and the count of detected spots is displayed.

