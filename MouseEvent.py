#impoting the libraries
import numpy as np
import cv2

#setting up the window 
winName = "win"
cv2.namedWindow(winName)
img = np.zeros((512, 512, 3), np.uint8)

#mouse call back function i.e when mouse is used this function will be activated
def drawCircle(event, x, y, flags, param):
    #if left mouse button is pressed twice
    if event == cv2.EVENT_LBUTTONDBLCLK:
        #draws a green circle
        cv2.circle(img, (x, y), 40, (0, 0, 255), -1)
    #if right mouse button is pressed twice
    if event == cv2.EVENT_RBUTTONDBLCLK:
        #makes the screen blank(black)
        img[:] = [0, 0, 0]
    
        
#method to call the callback function when mouse is used
cv2.setMouseCallback(winName, drawCircle)

#main function
def main():
    
    #continues until 'esc' key is pressed
    while(True):
        cv2.imshow(winName, img)
        if cv2.waitKey(1) == 27:
            break;
    
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()