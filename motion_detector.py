import cv2
import numpy as np

def main():
    
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame1 = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame2 = cap.read()
        
        #for getting motion that is difference between two frames
        d = cv2.absdiff(frame1, frame2)
        
        #to convert the color feed to black and white feed
        gray = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        
        #creating a gaussian blur to remove noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        
        #setting a binary threshold in order to draw contours easily
        ret, th = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
        
        #finding the contours on the basis of threshold feed
        img, c, h = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        #drawing the contours on the original color feed
        cv2.drawContours(frame1, c, -1, (0, 0, 255), 2)
        
        cv2.imshow('Prview', frame1)
        frame1 = frame2
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()