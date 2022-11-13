from turtle import left, right
import pyautogui as PAG
PAG.FAILSAFE = False
# tao tham so vi tri chuot
x,y = 1920-150,225

# chay ham click
count = 79
for index  in range(count):
    R,G,B = PAG.pixel(1602,315)
    if R != 93:
        PAG.rightClick(x,y)
        PAG.leftClick(x,y+125)
        PAG.leftClick(1635,410)
    else:
        PAG.rightClick(x,y)
        PAG.leftClick(x,y+160)
        PAG.leftClick(1635,410)
    print('Deleted user #',index)
        

PAG.alert("Successfully!")
        


    



