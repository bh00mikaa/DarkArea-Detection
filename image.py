# -*- coding: utf-8 -*-
"""
Real-time Dark Spot Detection using Laptop Camera
Reverted to original contrast enhancement (equalizeHist) and specific camera index.
"""

import cv2
import numpy as np
import os

def detect_dark_spots(frame):
    """
    Process a single frame to detect dark spots
    """
    # Step 1: Convert to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Histogram Equalization 
    equalized = cv2.equalizeHist(gray) 
    
    # Step 2: Apply Gaussian Blur
    blurred = cv2.GaussianBlur(equalized, (3, 3), 0)
    
    # Step 3: Apply Thresholding 
    _, thresh = cv2.threshold(blurred, 45, 255, cv2.THRESH_BINARY_INV) 
    
    # Step 4: Find Contours and Draw Bounding Boxes
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    output = frame.copy()
    spot_count = 0
    
    # Draw bounding boxes around detected dark spots
    
    for cnt in contours:
        if cv2.contourArea(cnt) > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            spot_count += 1
    
    # Add text overlay showing spot count
    cv2.putText(output, f'Dark Spots: {spot_count}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    return output, thresh, spot_count

# Camera initialization function remains as the simplified direct assignment 
def initialize_camera(camera_index=1):
    print(f"Attempting to open camera with index: {camera_index}")
    
    # Initialize camera with AVFoundation backend for macOS
    cap = cv2.VideoCapture(camera_index, cv2.CAP_AVFOUNDATION)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index}")
        print("Please ensure the camera is connected and not in use by another application.")
        return None

    # Set camera properties for better compatibility
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    # Test if we can actually read frames
    for attempt in range(5):
        ret, test_frame = cap.read()
        if ret and test_frame is not None:
            print(f"Camera {camera_index} test successful!")
            return cap
        print(f"Camera {camera_index} test attempt {attempt + 1}/5...")
        cv2.waitKey(200)
    
    print(f"Error: Camera {camera_index} opened but cannot read frames")
    cap.release()
    return None

def main():
    """
    Main function to run real-time dark spot detection
    """
    cap = initialize_camera() 
    save_folder = "saved_frames"
    os.makedirs(save_folder, exist_ok=True)
    
    if cap is None:
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    print("Camera initialized successfully!")
    print("Press 'q' to quit")
    print("Press 's' to save current frame")
    print("Press 't' to toggle threshold view")
    
    show_threshold = False
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        
        if not ret or frame is None:
            print("Warning: Failed to capture frame, retrying...")
            cv2.waitKey(100)
            continue
        
        processed_frame, threshold_frame, spot_count = detect_dark_spots(frame)
        
        if show_threshold:
            display_frame = cv2.cvtColor(threshold_frame, cv2.COLOR_GRAY2BGR)
            cv2.putText(display_frame, 'Threshold View - Press T to toggle',
                       (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        else:
            display_frame = processed_frame
            cv2.putText(display_frame, 'Normal View - Press T for threshold',
                       (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        
        cv2.imshow('Real-time Dark Spot Detection', display_frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            print("Quitting...")
            break
        elif key == ord('s'):
            filename = os.path.join(save_folder, f'darkspot_frame_{frame_count}.jpg')
            cv2.imwrite(filename, processed_frame)
            print(f"Frame saved as {filename}")
            frame_count += 1
        elif key == ord('t'):
            show_threshold = not show_threshold
            print(f"Threshold view: {'ON' if show_threshold else 'OFF'}")
    
    cap.release()
    cv2.destroyAllWindows()
    print("Camera released and windows closed")

if __name__ == "__main__":
    main()