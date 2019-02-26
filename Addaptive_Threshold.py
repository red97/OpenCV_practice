import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    path_name = "D:\\MOHNISH REDDY\\ml\\misc\\misc\\"
    img_path = path_name + "5.1.12.tiff"
    
    img = cv2.imread(img_path, 0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#    cv2.imshow('Win_test', img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    
    block_size = 73
    const = 10
    
    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, const)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, const)
    
    output = [img, th1, th2]
    title = ['Original', 'Mean', 'Gaussian']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(output[i], cmap = 'gray')
        
    plt.show()
    
if __name__ == "__main__":
    main()