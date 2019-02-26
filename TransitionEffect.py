import numpy as np
import cv2
import time

def main():
        
    path = "D:\\MOHNISH REDDY\\ml\\standard_test_images\\standard_test_images\\"
    imgpath1 = path + "mandril_color.tif"
    imgpath2 = path + "mandril_gray.tif"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    alpha = 0.0
    beta = 1.0
    gamma = 0.0
    
    while True:
        
        alpha = (alpha + 0.01)%1.0
        beta = 1.0 - alpha
        
        #(alpha*img1) + (beta*img2) + gamma
        output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
        cv2.imshow("Preview", output)
        
        if cv2.waitKey(1) == 27:
            break
        
        time.sleep(0.05)
        
        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()