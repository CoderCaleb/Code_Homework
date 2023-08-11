import os 
import cv2

to_dir = '/Users/caleb/Documents/PRO-C97_SIMPLE-PYTHON-PROGRAMS/PRO-C105/PRO-C105-Project-Images-main/Images'
pictures = os.listdir(to_dir)
Images = []
for picture in pictures:
    name, extension = os.path.splitext(picture)
    if extension in ['.png', '.jpg', '.jpeg']:
        file_name = os.path.join(to_dir,picture)
        Images.append(file_name)
        print(Images)

firstFrame = cv2.imread(Images[0])
height, width, channels = firstFrame.shape

dimensions = (width,height)
out = cv2.VideoWriter('/Users/caleb/Documents/PRO-C97_SIMPLE-PYTHON-PROGRAMS/PRO-C105/Project.avi',cv2.VideoWriter.fourcc(*'DIVX'),30,dimensions)

for image in Images:
    readImg = cv2.imread(image)
    out.write(readImg)

out.release()
print('Done')