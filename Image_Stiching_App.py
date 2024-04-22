import cv2
import numpy as np

def capture_video(duration=5, camera_index=1):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Cannot open the camera.")
        return []

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0  # Default to 30 FPS if unable to get FPS
    total_frames = int(fps * duration)
    frames = []
    frame_count = 0

    try:
        print("Capturing video...")
        while frame_count < total_frames:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break
            
         
            frames.append(frame)

            frame_count += 1
            cv2.imshow("frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return frames

def stitch_images(images):
    # Initialize SIFT
    sift = cv2.SIFT_create()

    # Start with the first image
    base = images[0]

    for img in images[1:]:
        kp1, des1 = sift.detectAndCompute(base, None)
        kp2, des2 = sift.detectAndCompute(img, None)

        # Matching features
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(des1, des2, k=2)

        # Apply Lowe's ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append(m)

        if len(good) > 10:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

            h, w = img.shape[:2]
            base = cv2.warpPerspective(base, M, (w + base.shape[1], h))

            # Adjust where the new image is placed in relation to the base
            overlap_w = int(w * 0.3)  # assuming 30% overlap
            base[0:h, overlap_w:overlap_w + w] = img

    return base

# Main code
video_frames = capture_video(10)
if video_frames:
    print("Stitching images...")
    panorama = stitch_images(video_frames)
    cv2.imshow('Panorama', panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No frames to process.")
