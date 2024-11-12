import cv2 as cv
import numpy as np


main_img = cv.imread('img/setblack.png', cv.IMREAD_ANYCOLOR)
temp_img = cv.imread('img/marcoinc.png', cv.IMREAD_ANYCOLOR)


if main_img is None or temp_img is None:
    print("Error loading images")

else:
    
    result = cv.matchTemplate(main_img, temp_img, cv.TM_CCOEFF_NORMED)

   
    threshold = 0.9

    
    loc = np.where(result >= threshold)

    
    num_matches = len(loc[0])

    print(f"Number Coin: {num_matches}")

    
    for pt in zip(*loc[::-1]): 
       
        topleft = pt
        dely = temp_img.shape[0]
        delx = temp_img.shape[1]
        bottomright = (topleft[0] + delx, topleft[1] + dely)

      
        cv.rectangle(main_img, topleft, bottomright, color=(255, 215, 196), thickness=1, lineType=cv.LINE_4)
        
        

        
        fontsize = 1
        font = cv.FONT_ITALIC
        posittion = (topleft[0] + 3, topleft[1] + 3)
        color = (255, 215, 196)
        cv.putText(main_img, "coin", posittion, font, fontsize, color, thickness=2)

   
    print(f"Total rectangles drawn: {num_matches}")

  
    cv.imshow("result", main_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    
    
