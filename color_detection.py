#importing the libraries
import cv2
import numpy as np

def main():
    
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret == True:
        
        ret, frame = cap.read()
        
        #converts BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #range to detect
        low = np.array([140, 150, 0])
        high =np.array([180, 255, 255])
        
        #image masking
        image_mask = cv2.inRange(hsv, low, high)
        
        #and operation of image masking and original
        output = cv2.bitwise_and(frame, frame, mask = image_mask)
        
        cv2.imshow("Image Mask", image_mask)
        cv2.imshow("Original Feed", frame)
        cv2.imshow("Only Blue Part", output)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    
    cap.release()
    
    
if __name__ == "__main__":
    main()