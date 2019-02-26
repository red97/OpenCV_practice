import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    img_path = "D:\\MOHNISH REDDY\\ml\\misc\\misc\\4.2.07.tiff"
    img = cv2.imread(img_path, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    r, g, b = cv2.split(img)
    
    plt.subplot(2, 2, 1)
    plt.title('1')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(cv2.merge((r, g, b)))
    
    plt.subplot(2, 2, 2)
    plt.title('1')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(r, cmap = 'gray')
    
    plt.subplot(2, 2, 3)
    plt.title('1')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(g, cmap = 'gray')
    
    plt.subplot(2, 2, 4)
    plt.title('1')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(b, cmap = 'gray')
    
    plt.show()
    
if __name__ == "__main__":
    main()