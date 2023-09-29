import cv2

body_classifier = cv2.CascadeClassifier('/Users/caleb/Code_Homework-1/PRO-106-ProjectTemplate-main/haarcascade_fullbody.xml')

cap = cv2.VideoCapture('/Users/caleb/Code_Homework-1/PRO-106-ProjectTemplate-main/walking.avi')

while True:
    
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    bodies = body_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 32:
        break

cap.release()
cv2.destroyAllWindows()
