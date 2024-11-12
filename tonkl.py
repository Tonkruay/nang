import cv2 as cv
import numpy as np

class Classbot:
    def __init__(self,main_img, temp_img):
        self.main_img = cv.imread('img/newmain.jpg',cv.IMREAD_ANYCOLOR)
        print ('main_img.shape')
        self.main_img = cv.imread('img/coin.png',cv.IMREAD_ANYCOLOR)
       
        
    def search(self):
        result = cv.matchTemplate(self.main_img,self.temp_img,cv.TM_CCOEFF_NORMED)
        print(result)
        minvalue,maxvalue,minloc,maxloc = cv.minMaxLoc(result)
        print(f'minvalue = {minvalue}maxvalue = {maxvalue}micloc = {minloc} and maxloc = {maxloc}')
        _, maxvalue, _,maxloc = cv.minMaxLoc(result)
        print(f'maxvalue = {maxvalue} and maxloc = {maxloc}')
        threshold = 0.5
        if maxvalue >= threshold:
            topleft = maxloc
            
            dely = self.temp_img.shape[0]
            delx = self.temp_img.shape[1]
            bottomright = (topleft[0]+delx,topleft[1]+dely)
            cv.rectangle(self.main_img,topleft,bottomright,color=(255, 215, 196),thickness=1,lineType=cv.LINE_4)
            fontsize = 1
            font = cv.FONT_ITALIC
            posittion = (topleft[0]+3,topleft[1]+3)
            color = (255,215,196)
            cv.putText(self.main_img,"",posittion,font,fontsize,color,thickness= 2)
            cv.imshow("result",self.main_img)
            cv.waitKey()
            cv.destroyAllWindows()  
mybot = Classbot('img/newmain.jpg','img/coin.png')
mybot.search()