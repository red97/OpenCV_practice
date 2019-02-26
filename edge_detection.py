import cv2
import numpy as np

def main():
    
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    #convolution matrix for edge detection (check wiki for more like sharpen, blur, etc)
    #https://en.wikipedia.org/wiki/Kernel_(image_processing)
    k = np.array([[-1, -1, -1], 
                 [-1, 8, -1], 
                 [-1, -1, -1]], np.float32)
        
    while ret:
        
        ret, frame = cap.read()
        
        #convolution of img matrix and convolution matrix(k) gives edge detection; -1 refers to depth of output is same as imput
        output = cv2.filter2D(frame, -1, k)
        cv2.imshow('Prview', output)
        
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
if __name__ == "__main__":
    main()