# MARK'S JOURNAL

## 2025 03 27 MV: 
- CONTINUED self-study
- FOUND BETTER video series to follow RE: how to connect Pixhawk 2.4.8 flight controller to RPi4 
- using Pixhawk Telemetry1 connector to 3-wires on RPi4's GPIO pin block!
- REFERENCE: https://www.youtube.com/watch?v=nIuoCYauW3s&t=6s  (watched on Rpi w NO audio; lip-read and read video description notes)
- ORDERED set of pixhawk telemetry connector-to-GPIO female pins on Amazon
- CONNECTED 6-pin connector to pixhawk Telemetry2 connector
- CONNECTED BLK wire to RPi GPIO GND (pin 9)
- CONNECTED WHT wire (Tx) to RPi GPIO Rx (pin 10)
- CONNECTED BLU wire (Rx) to RPi GPIO Tx (pin 8)
- TRIED powering Pixhawk by connecting RED wire (5V) to RPi GPIO 5V (pin 2) => NOTHING HAPPENED; Pixhawk DIDN'T POWER ON
- TRIED powering Pixhawk by connecting mini-USB to RPi USB3 (blue USB) => SUCCESS 1 Pixhawk IMMEIDATELY POWERED ON ! :-) 
- UPDATED readme
- SAVED | COMMITTED | PUSHED 



## 2025 03 08 MV: 
- CONTINUED self-study
- CREATED env ".venv"
- OPENED terminal with .venv activated
- pip install apriltag
- => ERROR: "Missing CMake" ? 
-    LEARNED this is a utility for CUSTOM-BUILDING pip install WHL files for python modules which contain "native" - HANDY !!
- pip install cmake => successful
- pip install opencv-python (contains CV2) => successful
- pip install apriltag => successful 
- SAVE | COMMIT | PUSH to github.com
- INSTALLED NEW WIFI ROUTER in house Netgear Nighthawk 
- UPDATED VSC on RPi using following download (for ARM64): https://update.code.visualstudio.com/latest/linux-deb-arm64/stable
- SWITCHED to new 5G WiFi network NETGEAR-41-5G
- SNAPPED pics of progress and TEXTED to MCV
- SAVE | COMMIT | PUSH to github.com
- SWITCHED CAMERAS !!! 
- - LEFT the "legacy" camera installed (port 0, not returning valid frames)
- - INSTALLED ordinary USB web cap (kind that clips onto laptop lid or top edge of external display) onto RPi's only USB3 port; 
- - CONFIGURED code so cam = cv2.VideoCapture(1)
- ADDED some additional exception-handling (really exception-printing is all) code just after cam.read()
- RAN Apriltag_video.py using VSC's RUN button
- => WORKING !!!!! 
- - a small pop-up window displays with a near-streaming picture first of whatever the CAMERA SEES, then IF there are AprilTags (ok to have SEVERAL) then it will: 
- - - DETECT each tag; 
- - - DRAW small green squares on the CORNERS of each AprilTag to PROVE that it UNDERSTANDS WHERE these corners ARE; and 
- - - DRAW the TAG ID in the CENTER of each AprilTag to PROVE that it UNDERSTANDS WHERE this center is as well ! 
- DEMO-ed to Michael
- UPDATED README
- SAVE | COMMIT | PUSH to github.com 
- PAUSED for the evening - need to R&D how to use this capability to help a DRONE carrying a 10 lb PAYLOAD LAND on a MOVING BOAT and MOVE VEHICLE !

## 2025 03 07 MV:
- BEGAN self-study
- RESEARCHED AptilTags
- SEARCHED for decent tutorial repos
- IDENTIFIED & SELECTED this one
- CLONED repo to RPI with external (USB) "Coral" GPU
- OPENED in VSC
- EXPLORED
- WATCHED VIDEOS
- PERUSED reference links (see below)
- PAUSED FOR DAY




===============================================================================
# Python_AprilTags
Test code to evaluate OpenCV and PyPi Apriltags Python module to detect FRC vision targets.
More info on the Apriltags module is available here: https://pypi.org/project/apriltag/

Also, FRC has some good info on their page:
https://docs.wpilib.org/en/stable/docs/software/vision-processing/apriltag/apriltag-intro.html

This year's game (2023) Charged Up will use Apriltags as well as retro-reflective vision targets.
https://www.firstinspires.org/robotics/frc/game-and-season

![alt text](https://github.com/atlee-circuitree/Python_AprilTags/blob/main/Apriltag_16h5_examples.png)
![alt text](https://github.com/atlee-circuitree/Python_AprilTags/blob/main/image.png)
