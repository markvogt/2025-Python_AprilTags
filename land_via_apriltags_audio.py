#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:45:29 2023

@author: rtb
"""
import apriltag
import cv2

from playsound import playsound


LINE_LENGTH = 5
CENTER_COLOR = (0, 255, 0)
CORNER_COLOR = (255, 0, 255)

### Some utility functions to simplify drawing on the camera feed
# draw a crosshair
def plotPoint(image, center, color):
    center = (int(center[0]), int(center[1]))
    image = cv2.line(image,
                     (center[0] - LINE_LENGTH, center[1]),
                     (center[0] + LINE_LENGTH, center[1]),
                     color,
                     3)
    image = cv2.line(image,
                     (center[0], center[1] - LINE_LENGTH),
                     (center[0], center[1] + LINE_LENGTH),
                     color,
                     3)
    return image

# plot a little text
def plotText(image, center, color, text):
    center = (int(center[0]) + 4, int(center[1]) - 4)
    return cv2.putText(image, str(text), center, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)



import numpy as np

def rotation_matrix_to_euler_angles(R):
    """
    Converts a rotation matrix to Euler angles (roll, pitch, yaw).
    R: 3x3 rotation matrix
    Returns: roll, pitch, yaw
    """
    sy = np.sqrt(R[0, 0]**2 + R[1, 0]**2)

    singular = sy < 1e-6  # Check for singularity

    if not singular:
        roll = np.arctan2(R[2, 1], R[2, 2])
        pitch = np.arctan2(-R[2, 0], sy)
        yaw = np.arctan2(R[1, 0], R[0, 0])
    else:
        roll = np.arctan2(-R[1, 2], R[1, 1])
        pitch = np.arctan2(-R[2, 0], sy)
        yaw = 0

    return np.degrees(roll), np.degrees(pitch), np.degrees(yaw)  # Convert to degrees

# Example rotation matrix...
# R = np.array([
#     [0.866, -0.5, 0],
#     [0.5, 0.866, 0],
#     [0, 0, 1]
# ])

# roll, pitch, yaw = rotation_matrix_to_euler_angles(R)
# print(f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")


# setup and the main loop... 
    
options = apriltag.DetectorOptions(families='tag16h5',
                                 border=1,
                                 nthreads=4,
                                 quad_decimate=1.0,
                                 quad_blur=0.0,
                                 refine_edges=True,
                                 refine_decode=False,
                                 refine_pose=False,
                                 debug=False,
                                 quad_contours=True)    

    
detector = apriltag.Detector(options=options)


# 2025 04 01 MV: RESEARCH via Bing Copilot yields decent APPROXIMATE/STARTING VALUES for a RUNCAM6 as follows:
fx = 1000    # 1000 pixels for an fx focal length...
fy = 1000    # 1000 pixels for an fy focal length...
cx = 960     # this is HALF of the WIDTH a 1920px by 1080px "HD" video frame...
cy = 540     # this is HALF of the HEIGHT of a 1920px by 1080px "HD" video frame...


# Assuming you have camera calibration data
camera_matrix = [
    [fx, 0, cx],
    [0, fy, cy],
    [0,  0,  1]
]
dist_coeffs = [0, 0, 0, 0]  # Assuming no distortion for simplicity


# INSTANTIATE a "camera" object connected to the USB3 serial port on RPis (port 1 if ribbon camera PRESENT, port 0 if ONLY camera connected)...
cam = cv2.VideoCapture(0)


if not cam.isOpened():
    print("Error: Could not access the camera.")
else:
    print("Camera is ready!")

looping = True

while looping:
    result, image = cam.read()


    if not result or image is None:
        print("Error: Failed to capture a valid frame.")
        break

    # print(f"Image shape: {image.shape if image is not None else 'None'}")


    try:
        grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception as ex: 
        print(f"ERROR converting image to grayscale > ex = {ex}...")


	# look for tags
    detections = detector.detect(grayimg)
    if not detections:
        print("Nothing")
    else:
	    # found some tags, report them and update the camera image
        for detect in detections:
            # print("tag_id: %s, center: %s" % (detect.tag_id, detect.center))
            image = plotPoint(image, detect.center, CENTER_COLOR)
            image = plotText(image, detect.center, CENTER_COLOR, detect.tag_id)
            for corner in detect.corners:
                image = plotPoint(image, corner, CORNER_COLOR)

            pose, e0, e1 = detector.detection_pose(
                detect,
                camera_params=(fx, fy, cx, cy),
                tag_size=0.16  # Replace with your tag size (in meters)
            )
            # print("Position (x, y, z):", pose[:3, 3])  # Translation
            R = pose[:3, :3]
            # print("Rotation matrix:", pose[:3, :3])    # Orientation

            roll, pitch, yaw = rotation_matrix_to_euler_angles(R)
            print(f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")


            # IMPLEMENT rudimentary audio feedback...
            if (yaw < -5):
                playsound("east.mp3")
            elif (yaw > 5):
                playsound("west.mp3")
            else:
                playsound("arrived.mp3")


	# refresh the camera image
    cv2.imshow('Result', image)
	# let the system event loop do its thing
    key = cv2.waitKey(100)
	# terminate the loop if the 'Return' key his hit
    if key == 13:
        looping = False

# loop over; clean up and dump the last updated frame for convenience of debugging
cv2.destroyAllWindows()
cv2.imwrite("final.png", image)