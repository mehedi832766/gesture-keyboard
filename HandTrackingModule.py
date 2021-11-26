import numpy as np
import imageio
import cv2

# Create black image 10x1
im = np.zeros([1,10,3], dtype=np.uint8)

# Fill with colours of rainbow and greys
im[0,0,:]=[255,0,0]       # red
im[0,1,:]=[255,165,0]     # orange
im[0,2,:]=[255,255,0]     # yellow
im[0,3,:]=[0,255,0]       # green
im[0,4,:]=[0,0,255]       # blue
im[0,5,:]=[75,0,130]      # indigo
im[0,6,:]=[238,130,238]   # violet
im[0,7,:]=[0,0,0]         # black
im[0,8,:]=[127,127,127]   # grey
im[0,9,:]=[255,255,255]   # white
imageio.imwrite("result.png",im)

hsv=cv2.cvtColor(im,cv2.COLOR_RGB2HSV)
print(hsv)