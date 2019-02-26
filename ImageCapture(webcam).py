#importing the libraries
import cv2
import matplotlib.pyplot as plt

#main function
def main():
    
    #to capture image from webcam
    cap = cv2.VideoCapture(0)
    
    #to check whether webcam is accesible or not
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    print(ret)
    print(frame)
    
    #converts the image from BGR to RGB
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #basic commands for displaying any image using matplotlib
    plt.imshow(img1)
    plt.title("capture")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    #to release the webcam after use
    cap.release()
    
if __name__ == "__main__":
    main()