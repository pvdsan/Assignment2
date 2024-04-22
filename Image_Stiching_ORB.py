import cv2
import numpy as np

def capture_images(num_images=4, camera_index=1):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Cannot open the camera.")
        return []

    images = []
    try:
        print("Press 'c' to capture an image. Press 'q' to quit after capturing all images.")
        while len(images) < num_images:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break
            
            cv2.imshow("Camera", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('c'):
                images.append(frame)
                print(f"Captured {len(images)} of {num_images} images.")
            elif key == ord('q') and len(images) == num_images:
                print("Quitting capture.")
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
    
    return images

def stitch_images(images):
    sift = cv2.SIFT_create()
    base = images[0]

    for img in images[1:]:
        kp1, des1 = sift.detectAndCompute(base, None)
        kp2, des2 = sift.detectAndCompute(img, None)

        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(des1, des2, k=2)

        good = [m for m, n in matches if m.distance < 0.75 * n.distance]
        if len(good) > 3:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            h, w = img.shape[:2]
            base = cv2.warpPerspective(base, M, (w + base.shape[1], h))

            overlap_w = int(w * 0.3)
            base[0:h, overlap_w:overlap_w + w] = img

    return base

# Main code
images = capture_images()
if images:
    print("Stitching images...")
    panorama = stitch_images(images)
    cv2.imshow('Panorama', panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No images to process.")
