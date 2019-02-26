#importing the libraries
import numpy as np
import cv2

#setting up the window
winName = "window"
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(winName)

#drawing tell whether to draw or not
drawing = False
#mode tell what to draw
mode = False
#for starting position of rectangle
(ix, iy) = (-1, -1)

def draw_shape(event, x, y, flags, param):
    
    global ix, iy, drawing, mode
    #if left button is pressed drwaing is true and ix and iy are set to the current position
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y
    
    #when the mouse is moving while left button is pressed sth is drawn
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        
    #when left button is no longer being pressed we make drawing false so nothing would be drawn        
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
 #       if mode == True:
 #           cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
 #       else:
 #           cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
            
cv2.setMouseCallback(winName, draw_shape)
                    
def main():
    
    global mode
    
    while(True):
        cv2.imshow(winName, img)
        k = cv2.waitKey(1)
        
        if(k == ord('m') or k == ord('M')):
            mode = not mode
        elif k == 27:
            break;
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()