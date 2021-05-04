import cv2 as cv
import numpy as np
import math

name = input("Full name of file (With type)? ")
a = name.split(".")
type = a[1]

img = cv.imread(name)

def resized_array(img,k): #create new big array
	img_size=img.shape
	return np.zeros((img_size[0]*k,img_size[1]*k,img_size[2]))

def interpolation(x,y,img,k): #lineal interpolation to fill voids in big array
	size=int(2*k)
	kf=1/(size-1)
  
	new_square=[[0]*size for i in range(size)]
  
	a=img[x][y]
	b=img[x+1][y]
	c=img[x][y+1]
	d=img[x+1][y+1]
  
	for x1 in range(0,size):
		for y1 in range(0,size):
			x_value=x1*kf
			y_value=y1*kf
			new_square[x1][y1]=a*(1-x_value)*(1-y_value)+b*x_value*(1-y_value)+c*(1-x_value)*y_value+d*x_value*y_value #lineal interpolation method
	  
	return new_square
  
def resized_image(img,new_array,k):

	img2=new_array
  
	for x1 in range(0,img.shape[0],2):
		for y1 in range(0,img.shape[1],2):
			try:
				new_square=interpolation(x1,y1,img,k)
			except:															
				continue
	  
			for x1_new in range(0,2*k):
				for y1_new in range(0,2*k):
		
					try:															# The try/except
						img2[x1*k+x1_new][y1*k+y1_new]=new_square[x1_new][y1_new]	# used to catch OutOfRange
					except:															# except and skip
						continue													# them
			
	return img2

k = int(input("K? "))
aboba = resized_array(img,k)
img2 = resized_image(img,aboba,k)
cv.imwrite((input("Name of output file? ")+ "." + type),img2)