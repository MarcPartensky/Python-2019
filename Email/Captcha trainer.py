from selenium import webdriver
from PIL import Image
import numpy as np
import time

url="https://patrickhlauke.github.io/recaptcha/"


def searchCaptcha(filename):
    Img=Image.open(filename)
    img=np.array(Img)
    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y][x][0]!=39: continue
            if img[y][x][1]!=67: continue
            if img[y][x][2]!=153: continue
            if img[y][x][3]!=255: continue
            color00=list(img[y][x])
            color10=list(img[y][x+1])
            color01=list(img[y+1][x])
            color11=list(img[y+1][x+1])
            if not (color00==[39,67,153,255] and color10==[38,68,164,255] and color01==[38,68,151,255] and color11==[37,66,158,255]):
                continue
            X=x-234
            Y=y+34
            return [X,Y]
    return None


def resolveCaptcha(url):
    driver=webdriver.Chrome('/Users/olivierpartensky/Programs/Library/Selenium/chromedriver')
    action=webdriver.common.action_chains.ActionChains(driver)
    driver.get(url)
    #action.move_by_offset(36,156)
    #gris en 27 138 => [193,193,193,255]
    #bleu claire 270 127 => [39,67,153,255]
    #36-270=
    #151-127=
    #36 151 middle
    result=searchCaptcha("training.png")
    print(result)
    if not result:
        raise Exception("Captcha could not be found.")
    action.move_by_offset(result[0],result[1])
    action.click()
    action.perform()


    #driver.save_screenshot("training.png")

resolveCaptcha(url)


"""
[ 39  67 153 255]
[ 38  68 164 255]
[ 38  68 151 255]
[ 37  66 158 255]
"""
#Img.show()


"""

imin,imax=200,255
img2=[[255*(img[y][x]-imin)/(imax-imin) for x in range(len(img[0]))] for y in range(len(img))]

noise=np.random.normal(0,7,img.shape)
Img3=Image.fromarray(img+noise).convert("L")
Img3.show()
Img3.filter(ImageFilter.BoxBlur(1)).show()
Img3.show()
"""
