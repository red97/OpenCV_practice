import cv2
import numpy as np

def main():
    
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()
#        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#        output = cv2.filter2D(frame, -1, k)
        output = cv2.Canny(frame, 50, 250, apertureSize=5, L2gradient=True)
        cv2.imshow('Prview', output)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()