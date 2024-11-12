import cv2 as cv
main_lmg = cv.imread('img/ra25.png',cv.IMREAD_ANYCOLOR)
print('main_img.shape')
temp_img = cv.imread('img/ra25-1.png',cv.IMREAD_ANYCOLOR)
print(temp_img)     
print(temp_img.shape[1])
result = cv.matchTemplate(main_lmg,temp_img,cv.TM_CCOEFF_NORMED)
print(result)
minvalue,maxvalue,minloc,maxloc = cv.minMaxLoc(result)
print(f'minvalue = {minvalue}maxvalue = {maxvalue}micloc = {minloc} and maxloc = {maxloc}')
_, maxvalue, _,maxloc = cv.minMaxLoc(result)
print(f'maxvalue = {maxvalue} and maxloc = {maxloc}')
threshold = 0.5
if maxvalue >= threshold:
    topleft = maxloc
    
    dely = temp_img.shape[0]
    delx = temp_img.shape[1]
    bottomright = (topleft[0]+delx,topleft[1]+dely)
    cv.rectangle(main_lmg,topleft,bottomright,color=(255, 215, 196),thickness=1,lineType=cv.LINE_4)
    fontsize = 1
    font = cv.FONT_ITALIC
    posittion = (topleft[0]+3,topleft[1]+3)
    color = (255,215,196)
    cv.putText(main_lmg,"Tonkla",posittion,font,fontsize,color,thickness= 2)
cv.imshow("result",main_lmg)
cv.waitKey()
cv.destroyAllWindows()