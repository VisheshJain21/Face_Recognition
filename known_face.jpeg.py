import cv2


def capture_image():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open webcam.")
        return

    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Release the webcam
    cap.release()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Unable to capture frame.")
        return

    # Save the captured frame as an image file
    cv2.imwrite('known_face.jpeg', frame)
    print("Reference image saved as 'known_face.jpeg'.")


# Call the function to capture an image
capture_image()
