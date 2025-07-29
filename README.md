# DarkArea-Detection
This Python project uses OpenCV to detect dark spots in real-time using a laptop's built-in or external camera. It processes each video frame to identify dark regions based on intensity, draws bounding boxes around them, and provides a live count overlay. The detected frames can also be saved with a single keypress.

Features

Real-time video capture and processing using OpenCV
Histogram equalization for contrast enhancement
Gaussian blur and thresholding for spot segmentation
Contour detection to locate dark spots
Bounding box visualization and count overlay
Toggle between normal and threshold views
Save snapshots into a dedicated folder (saved_frames/)


Controls

Press q → Quit the program
Press s → Save the current frame to saved_frames/
Press t → Toggle between normal and threshold views
