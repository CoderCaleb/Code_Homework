import cv2

planetsPic = cv2.imread('/Users/caleb/Documents/PRO-C97_SIMPLE-PYTHON-PROGRAMS/PRO-C104/PRO-104-Project-Image-main/solar-system.jpg')
cv2.putText(planetsPic,'Sun',(30,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Moon',(125,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Venus',(200,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Earth',(295,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Mars',(390,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Jupiter',(525,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Saturn',(800,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Uransus',(965,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
cv2.putText(planetsPic,'Neptune',(1125,planetsPic.shape[0]//2),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)

cv2.imshow('Solar System',planetsPic)
cv2.waitKey(0)
cv2.destroyAllWindows()