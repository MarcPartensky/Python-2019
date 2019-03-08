from PIL import Image,ImageFilter
import numpy as np
import matplotlib.pyplot as plt
#import sys

#print(sys.version)

Img=Image.open("simba.png")
img=np.array(Img)
Img.show()

imin,imax=200,255
img2=[[255*(img[y][x]-imin)/(imax-imin) for x in range(len(img[0]))] for y in range(len(img))]

noise=np.random.normal(0,7,img.shape)
Img3=Image.fromarray(img+noise).convert("L")
Img3.show()
Img3.filter(ImageFilter.BoxBlur(1)).show()
Img3.show()

#Img2=Image.fromarray(img2).convert("L")
#Img2.show()



#img2.show()
#img.show()

#w,h=img.size
#print(w,h)

#print(img.__dict__)
#print(rimg["im"])

#for key,value in rimg.__dict__.items():
    #print(key,":",value)

#px_value=img.getpixel((20,100))
#print(px_value)

#mat=np.array(img)
#print(mat)
#print(mat.shape)

n,bins,patches=plt.hist(img.flatten(),bins=range(256))
plt.show()
