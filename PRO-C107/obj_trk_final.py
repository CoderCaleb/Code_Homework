import cv2
import time
import math

p1 = 530
p2 = 300

xs = []
ys = []

video = cv2.VideoCapture("/Users/caleb/Code_Homework-1/project-C107-template-main/footvolleyball.mp4")
# Load tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
success, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("tracking", img, False)

# Initialize the tracker on the img and the bounding box
tracker.init(img, bbox)

def goal_track(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    c1 = x + int(w / 2)
    c2 = y + int(h / 2)
    cv2.circle(img, (c1, c2), 2, (0, 0, 255), 5)

    cv2.circle(img, (int(p1), int(p2)), 2, (0, 255, 0), 3)
    dist = math.sqrt(((c1 - p1) ** 2) + (c2 - p2) ** 2)
    print(dist)

    if dist <= 20:
        cv2.putText(img, "Goal", (300, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs) - 1):
        cv2.circle(img, (xs[i], ys[i]), 2, (0, 0, 255), 5)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

while True:
    # Read the video and store the values in check and img variables
    success, img = video.read()

    # Use the tracker.update() and store the values in the success and bbox variables
    success, bbox = tracker.update(img)

    # Check if we are getting the updated image
    if success:
        # Call drawBox() and pass img and bbox
        drawBox(img, bbox)
    else:
        # Put the text on the screen saying “LOST”
        cv2.putText(img, "LOST", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Call the goal_track() function and pass img and bbox as parameters to it
    goal_track(img, bbox)

    # Call the cv2.imshow() function to show the image
    cv2.imshow("hand tracking", img)

    # Use the 'q' key to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
