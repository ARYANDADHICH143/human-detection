import cv2
import numpy as np
import imutils
import argparse
from imutils.object_detection import non_max_suppression

out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'MJPG'),15.,(640,480))

HOGCV=cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
def detect(frame):
    
    boundingboxes,weights=HOGCV.detectMultiScale(frame,winStride=(4,4),padding=(8,8),scale=1.03)
    boundingboxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boundingboxes])
    person=1
    
    
    for (xA, yA, xB, yB) in boundingboxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        person=person+1
    cv2.putText(frame, f'No of people : {person-1}', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)    
    return frame
def detectImage():
    image=cv2.imread("C:/Users/user/Desktop/project-final/download.jpg")
    image=imutils.resize(image,width=min(800,image.shape[1]))
    result=detect(image)
    cv2.imshow("Output",result)
    cv2.waitKey(0)

def detectVideo():
    video = cv2.VideoCapture('C:/Users/user/Desktop/project-final/vedio7.mp4') 

    while video.isOpened():
        check,frame=video.read()
        if check:
            frame=imutils.resize(frame,width=min(400,frame.shape[1]))
            frame=detect(frame)
            out.write(frame.astype('uint8'))
            cv2.imshow("Output",frame)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
    
def detectCamera():
    video = cv2.VideoCapture(0) 

    while True:
        check,frame=video.read()
        if check:
            frame=imutils.resize(frame,width=min(400,frame.shape[1]))
            frame=detect(frame)
            cv2.imshow("Output",frame)
            if cv2.waitKey(25) & 0xFF==ord('q'):
                break
        else:
            break
    video.release()
            
detectVideo()