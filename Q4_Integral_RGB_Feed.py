import cv2
import numpy as np

def compute_integral_image(image):
    # Convert image to grayscale for simplification
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Initialize the integral image with zeros and the same data type but use uint64 to prevent overflow
    integral_image = np.zeros((gray_image.shape[0] + 1, gray_image.shape[1] + 1), dtype=np.uint64)
    
    # Compute the integral image by cumulative sum approach
    for y in range(1, integral_image.shape[0]):  # Start from 1 to accommodate the initial zero row
        sum_row = 0
        for x in range(1, integral_image.shape[1]):  # Start from 1 to accommodate the initial zero column
            sum_row += gray_image[y - 1, x - 1]
            integral_image[y, x] = integral_image[y - 1, x] + sum_row

    return integral_image[1:, 1:]  # Return the correct size by slicing off the zeroed row and column

def main():
    # Start video capture from default camera
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame capture failed.")
            break

        # Compute the integral image using the manual method
        integral_img_manual = compute_integral_image(frame)


        # Display the original image
        cv2.imshow('Original Image', frame)

        # Display the manually calculated integral image (scaled for better visualization)
        display_integral_manual = cv2.convertScaleAbs(integral_img_manual / integral_img_manual.max() * 255)
        cv2.imshow('Integral Image (Manual)', display_integral_manual)



        # Break the loop with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release capture and destroy all windows when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
