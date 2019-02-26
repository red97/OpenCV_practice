import cv2
import numpy as np
def emptyFn():
    pass
def main():
    
    track_win = 'Tracks'
    img1 = np.zeros((512, 512, 3), np.uint8)
    cv2.imshow(track_win, img1)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    cv2.createTrackbar('low_1', track_win, 0, 255, emptyFn);
    cv2.createTrackbar('low_2', track_win, 0, 255, emptyFn);
    cv2.createTrackbar('low_3', track_win, 0, 255, emptyFn);
    cv2.createTrackbar('high_1', track_win, 0, 255, emptyFn);
    cv2.createTrackbar('high_2', track_win, 0, 255, emptyFn);
    cv2.createTrackbar('high_3', track_win, 0, 255, emptyFn);
    while True:
        
        cv2.imshow(track_win, img1)
        ret, frame = cap.read()
        #converts BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        l1 = cv2.getTrackbarPos('low_1', track_win)
        l2 = cv2.getTrackbarPos('low_2', track_win)
        l3 = cv2.getTrackbarPos('low_3', track_win)
        h1 = cv2.getTrackbarPos('high_1', track_win)
        h2 = cv2.getTrackbarPos('high_2', track_win)
        h3 = cv2.getTrackbarPos('high_3', track_win)
        print(l1,l2,l3)
        print(h1,h2,h3)
        
        #range to detect
        low = np.array([l1, l2, l3])
        high =np.array([h1, h2, h3])
        
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