import cv2

# Create our body classifier
body_classifier = cv2.CascadeClassifier('/Users/caleb/Code_Homework-1/PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('/Users/caleb/Code_Homework-1/PRO-106-ProjectTemplate-main/walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    # Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Extract bounding boxes for any bodies identified
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    # Display the frame with rectangles drawn around bodies
    cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 32: # 32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
