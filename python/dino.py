# Igor bot

from PIL import ImageGrab, Image
import time
import pyautogui

lastTime = None
debug_time = False


def screenShotSecondMonitor():
    global lastTime
    global debug_time
    # boxSecondDisplay = (2561, 0, 4480, 1080)
    boxDino = (2640, 400, 4000, 720)
    # screen = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False, xdisplay=None)
    # screen = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None)
    # screen = ImageGrab.grab(bbox=boxDino, all_screens=True)
    screen = ImageGrab.grab()
    # screen.save("igor2.jpg")
    # screen.save("semTreco.jpg")

    if debug_time:
        actualTime = time.perf_counter()
        if lastTime is not None:
            print(actualTime - lastTime)
        lastTime = actualTime

    return screen


# Just save two images to help calibrate the screen
def screenModel():
    screenUpName = "screenUp.jpg"
    screenDownName = "screenDown.jpg"
    time.sleep(3)
    pyautogui.press("space")
    screenUp = ImageGrab.grab(bbox=None, all_screens=True)
    time.sleep(1)
    pyautogui.keyDown("down")
    screenDown = ImageGrab.grab(bbox=None, all_screens=True)
    screenUp.save(screenUpName)
    screenDown.save(screenDownName)
    pyautogui.keyUp("down")


def jump():
    print("jumped!")
    pyautogui.keyUp("down")
    pyautogui.press("space")


def down():
    # print("Down!")
    pyautogui.keyDown("down")


def screenShot():
    # 1610, 1040
    original = "igor.jpg"
    # h = 550
    MIN_H = 620
    increment = 0


    MIN_V_JUMP = 640 + 10
    MIN_V_DOWN = 580 + 3
    SQUARE_H = 100
    SQUARE_V = 1
    temporaria = "temporaria.jpg"



    offSet = 0
    base = 3900
    count = base
    jumpFlag = False
    downFlag = False
    color = ""
    refColor = ""
    while (count > 0):
        count -= 1
        screen = screenShotSecondMonitor()

        # SKY color
        refColor = screen.getpixel((100, 200))
        for h in range(MIN_H, MIN_H + SQUARE_H):
            for v in range(0, + SQUARE_V):
                colorJump = screen.getpixel((h + int(offSet), v + MIN_V_JUMP))
                colorDown = screen.getpixel((h + int(offSet), v + MIN_V_DOWN))
                if (colorJump != refColor):
                    jumpFlag = True
                    break
                elif (colorDown != refColor):
                    downFlag = True
                    break

            if jumpFlag or downFlag:
                limitValue = 1920 - MIN_H - SQUARE_H
                nowTime = time.perf_counter()
                print(nowTime)

                if 22 < nowTime < 26:
                    offSet = 86
                elif 32 < nowTime < 34:
                    offSet = 148
                elif 40 < nowTime < 41:
                    offSet = 264
                elif 48 < nowTime < 49:
                    offSet = 290
                elif 69 < nowTime < 72:
                    offSet = 510
                elif 88 < nowTime < 89:
                    offSet = 650
                elif 117 < nowTime < 120:
                    offSet = 850

                if offSet > limitValue:
                    offSet = limitValue

                break

        if jumpFlag:
            jump()
            # print(str(count) + ": " + str(color))
            # pyautogui.keyUp("down")
            # print("jumped!")
            # pyautogui.press("space")
            jumpFlag = False
        elif downFlag:
            down()
            downFlag = False
        # else:
        #     pyautogui.keyDown("down")
        #     # pyautogui.press("down")

    # screen.show()
    # screen.save(original)
    # screen.thumbnail((128,128))
    print("\nIgor")


print("Starting in 3s ...")

time.sleep(0.5)
pyautogui.click((371,603))
# pyautogui.moveTo((371,603))
pyautogui.click((422,803))
time.sleep(0.2)
pyautogui.moveTo((371,603))
time.sleep(2.1)
print("Started!!!")
# pyautogui.click(2560+ MIN_H, MIN_V_JUMP)
jump()
screenShot()
# screenModel()
# while True:
#     print(pyautogui.position())
    # print(time.perf_counter())
#     time.sleep(1)
print("finish!!!")

