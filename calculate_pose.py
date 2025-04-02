import cv2
import apriltag

# Initialize detector
options = apriltag.DetectorOptions(families="tag16h5")
detector = apriltag.Detector(options)

# Example grayscale image
gray_image = cv2.imread("tag_image.jpg", cv2.IMREAD_GRAYSCALE)
detections = detector.detect(gray_image)

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

# Iterate through detections to extract pose
for detection in detections:
    pose, e0, e1 = detector.detection_pose(
        detection,
        camera_params=(fx, fy, cx, cy),
        tag_size=0.16  # Replace with your tag size (in meters)
    )
    print("Position (x, y, z):", pose[:3, 3])  # Translation
    print("Rotation matrix:", pose[:3, :3])    # Orientation
