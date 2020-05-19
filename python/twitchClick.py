# Igor
# This script checks for some green box in the second monitor to click on it.

from PIL import ImageGrab, Image
import time
import pyautogui


def screenShotSecondMonitor():
    boxSecondDisplay = (2561, 0, 4480, 1080)
    screen = ImageGrab.grab(bbox=boxSecondDisplay, all_screens=True)
    # screen.save("igor2.jpg")
    return screen


def clickOnScreen():
    print("clicar!!!")
    # Orignal position
    original = pyautogui.position()
    # Move to Click Position
    # pyautogui.moveTo(3858,838)
    # click
    pyautogui.click(3858, 838)
    # Come back to Original position
    # time.sleep(3)
    pyautogui.moveTo(original)


def screenShot():
    # 1610, 1040
    h = 1618
    v = 1064

    count = 72000
    while count > 0:
        count -= 1
        screen = screenShotSecondMonitor()
        color = screen.getpixel((h, v))
        # print(str(count) + ": " + str(color))
        # print("Original" + str(pyautogui.position()))
        if 220 < color[1] < 240:
            clickOnScreen()
        time.sleep(10)


screenShot()
