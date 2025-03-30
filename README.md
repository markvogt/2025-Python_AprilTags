# MARK'S JOURNAL

## 2025 03 28 MV: 
- CONTINUED efforts to get Pixhawk 2.4.8 flight controller integrated with RPi (still installing code)
- NOTE: it appears that even when adhering to the best practice of employing python VIRTUAL ENVIRONMENTS (mine is /.venv/) there are STILL python packages which MUST also be installed at the SYSTEM/default/OS level, using "sudo apt-get install <package name>  - very confusing, except if you consider that these contain C++ code that must be BUILT for a SPECIFIC PLATFORM, and then the regular-schmegular python packages in /.venv/ EXPECT these system-level packages to be present ? 
- DELETED virtual environment /.venv - ONLY USING SYSTEM install of python !!! 
- REPEATED all package installs (including sudo apt-get installs of platform-specific packages) per the video listed in 2025 03 27

- REFERENCE: INSTALLED following packages using the exact commands provided ONE AT A TIME: 
-    Raspberry Pi:
-    $ sudo raspi-config
-    $ sudo nano /boot/config.txt
-    $ sudo reboot
-    $ sudo apt-get update
-    $ sudo apt-get install python3-pip
-    $ sudo apt-get install python3-dev python3-opencv python3-wxgtk4.0 python3-matplotlib python3-lxml libxml2-dev libxslt-dev
-    $ sudo pip install PyYAML mavproxy
-    $ sudo mavproxy.py --master=/dev/ttyAMA0

- TRIED running > sudo mavproxy.py --master=/dev/tty/AMA0
- => UNSUCCESSFUL :-( threw errors 
- TRIED simply running mavproxy.py  (hoping it could AUTO-DETECT the presence of a flight controller)
- => SUCCESSFUL !!! detected the Pixhawk on "line 0" 
- UPDATED readme 
- SAVED | COMMITTED | PUSHED


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
- DISCONNECTED my "Coral" USB-connecte external GPU (running non-stop for MORE THAN 2 YEARS NOW) from USB3 port of RPi
- CONNECTED Pixhawk by connecting mini-USB to RPi USB3 (blue USB) 
- => SUCCESS !!! Pixhawk IMMEIDATELY POWERED ON ! :-) 
- UPDATED readme
- SAVED | COMMITTED | PUSHED 
- CHARGED new RUNCAM6 sports cam from Michael 
- UNINSTALLED existing USB webcam (LogiTech) from USB port of RPi
- INSTALLED RUNCAM6 into RPi USB2 port using provided USB-micro to USB-A 10 inch cable 
- LEFT CAM port set to 0 since STILL the ONLY camera connected
- RAN Apriltag_video.py using VSC "run" button
- => WORKING !!!!
- PAUSED for few hours (tennis break on a Friday afternoon/evening)
- CONTINUED with Pixhawk-to-RPi integration
- CONTINUED installation of various python modules into virtual env  /.venv 
- REALIZED I MIGHT have been installing much of what's required into the SYSTEM install of PYTHON3 :-O !!! 
- - pip list on /.venv shows only about 7 packages installed :-( 
- - pip list in OS terminal windows (NOT integrated terminal in VSC) shows DOZENS of packages installed :-O !!! 
- WHAT TO DO ???
- HOW BEST TO PROCEED ??? 
- DECISION: continue install of remaining packages into but /.venv  (virtual environment - NOT system/default env)
- performed (.venv) > pip install PyYAML
- => SUCCESSFULLY installed in (.venv)!
- performed (.venv) > pip install mavproxy
- => SUCCESSFULLY instlled in (.venv) ! - INCLUDING all auto-detected DEPENDENCIES (but not those mentioned in the video???)
- IMPORTANT NOTE: sudo pip install performs a SYSTEM install and throws EXCEPTTIOS; regular-schmegular (.venv) pip install <packages> works!
-- performed (.venv) > pip install wxPython in lieu of SYSTEM install of python3-wxgtk4.0
- => ERRORS; but (.venv) > pip list shows wxPython IS installed !!! 
- PAUSED for evening


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
