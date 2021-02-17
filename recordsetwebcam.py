import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)

cap.set(3,320) #set heigt   >>refer propId
cap.set(4,240)  #set width
#cap.set(5,30)   #fps,value
#cap.set(10,0.5) #brightnes,value
#cap.set(11,0.2) #contrast,value

time.sleep(0.1)



while True:
    ret,frame = cap.read()

    
    fps = cap.get(5)
    #print (fps)
    
    
    
    cv2.imshow('frame',frame)


    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
