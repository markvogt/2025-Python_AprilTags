#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:45:29 2023

@author: rtb
"""
import apriltag
import cv2


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

# setup and the main loop
    
    
    
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


# INSTANTIATE a "camera" object connected to the built-in "legacy" ribbon cable on RPis (port 0)...
# cam = cv2.VideoCapture(0)
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

    print(f"Image shape: {image.shape if image is not None else 'None'}")


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
            print("tag_id: %s, center: %s" % (detect.tag_id, detect.center))
            image = plotPoint(image, detect.center, CENTER_COLOR)
            image = plotText(image, detect.center, CENTER_COLOR, detect.tag_id)
            for corner in detect.corners:
                image = plotPoint(image, corner, CORNER_COLOR)
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