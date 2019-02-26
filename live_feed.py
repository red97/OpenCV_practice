#importing the libraries
import cv2

#setting up the window
winName = "LiveFeed"
cv2.namedWindow(winName)

def main():
    
    #to capture image from webcam
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
     
    #while webcam is on    
    while ret:
        
        ret, frame = cap.read()
        cv2.imshow(winName, frame)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    
    cap.release()
    
if __name__ == "__main__":
    main()