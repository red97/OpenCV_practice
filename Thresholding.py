import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    path_name = "D:\\MOHNISH REDDY\\ml\\misc\\misc\\"
    img_path = path_name + "7.1.05.tiff"
    
    img = cv2.imread(img_path, 0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#    cv2.imshow('Win_test', img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    
    #threshold values and max value th = 0 for 'otsu threshold' any other value for mannual
    #otsu is used when bg and foreground are very similar and we need to differentiate
    th = 0
    max_val = 255
    
    #basic commands for threshold algos
    ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
    
    output = [img, o1, o2, o3, o4, o5]
    title = ['Original', 'Binary', 'Inv Binary', 'Zero', 'Inv Zero', 'Trunc']
    
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(output[i], cmap = 'gray')
        
    plt.show()
    
if __name__ == "__main__":
    main()