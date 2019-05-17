from PIL.Image import *
from glob import *
import os

def images_in_list (path):
    os.chdir(path)
    imglist=[]
    
    for i in range (0,len(glob("*png"))):
        imglist.append(glob("*png")[i])
        img_medium_color(imglist[i])
        
    for i in range (0,len(glob("*jpg"))):
        imglist.append(glob("*jpg")[i])
        img_medium_color(imglist[i])
        
    for i in range (0,len(glob("*jpeg"))):
        imglist.append(glob("*jpeg")[i])
        img_medium_color(imglist[i])       
        
def img_medium_color (img):
    print(img)
    img=open(img)
    width, height = img.size
    size=width*height
    rsomme,gsomme,bsomme=0,0,0
    
    for x in range (width):
        for y in range (height):
            c = Image.getpixel(img, (x, y))
            rsomme +=c[0]
            gsomme +=c[1]
            bsomme +=c[2]
    print(rsomme/size,gsomme/size,bsomme/size)



        

img_medium_color("63858699_p0_master1200_out2.jpg")
images_in_list("IMAGES")
