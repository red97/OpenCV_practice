#importing the libraries
import numpy as np
import cv2

#dummy function
def emptyFn():
    pass

#main function
def main():
    
    #creates a black window
    img1 = np.zeros((512, 512, 3), np.uint8)
    #name of the window
    windowName = 'image'
    #we set the the window with the given name
    cv2.namedWindow(windowName)
    
    
    #creates a track bar which can be used to change the value from of 0 to 255
    #'B' -> label, windowName -> on which window to perform, (0, 255)-> range, emptyFn->function associated with trackbar
    cv2.createTrackbar('B', windowName, 0, 255, emptyFn)
    cv2.createTrackbar('G', windowName, 0, 255, emptyFn)
    cv2.createTrackbar('R', windowName, 0, 255, emptyFn)
    
    #this continue until 'esc' key is pressed
    while(True):
        #to display the image
        cv2.imshow(windowName, img1)
        #for recognizing the 'esc' key
        if cv2.waitKey(1) == 27:
            break;
            
        #takes value from the track bar and puts in a variable
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)
        
        #we fill the image with the value we have recieved from the trackbar
        img1[:] = [blue, green, red]
       
    #after the while loop has stopped it closes all the windows
    cv2.destroyAllWindows()
    
    
#to call the main function
if __name__ == "__main__":
    main()