 
import cv2
import os
import numpy as np

def green_detect(file_name):
	folder='uploads'

	img1 = cv2.imread(os.path.join(folder,file_name))

        green = np.uint8([[[0,255,0]]])
        hsv_color = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
        h_c = hsv_color[0][0][0]

        lowerColor = np.array([h_c -10,100,100])
        upperColor = np.array([h_c +10,255,255])
        print(hsv_color)

        image = cv2.imread('algae.jfif')
        hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        mask_image = cv2.inRange(hsv_image, lowerColor,upperColor)
        final_image = cv2.bitwise_and(image,image,mask=mask_image)

        #cv2.imwrite('C:/Users/Lenovo/Downloads/cv2-hsv.png',hsv_image)
        #cv2.imwrite('C:/Users/Lenovo/Downloads/cv2-mask.png',mask_image)
        #cv2.imwrite('C:/Users/Lenovo/Downloads/cv2-final.png',final_image)
        
	cv2.imwrite(os.path.join(folder,file_name),hsv_image)
	cv2.imwrite(os.path.join(folder,file_name),mask_image)
	cv2.imwrite(os.path.join(folder,file_name),final_image)
