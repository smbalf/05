import os
import cv2
import pyautogui
from pywinauto import Application
import numpy as np

image_folder = "images"
tree_stump_images = {}

for i in range(1, 2):
    tree_image = os.path.join(image_folder, f"tree{i}.png")
    stump_image = os.path.join(image_folder, f"stump{i}.png")
    tree_stump_images[tree_image] = stump_image

app = Application().connect(title="Scape05 - the massive online adventure game - World 53")
app.top_window().set_focus()


while True:
    tree_location = None

    for tree_image, stump_image in tree_stump_images.items():
        tree_img = cv2.imread(tree_image)
        gray_tree_img = cv2.cvtColor(tree_img, cv2.COLOR_BGR2GRAY)
        screen =  pyautogui.screenshot()
        screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screen_gray, gray_tree_img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        if loc[0].size > 0:
            tree_location = (loc[1][0],loc[0][0],tree_img.shape[1],tree_img.shape[0])
            print("Found a tree!")
            break

    if tree_location is not None:
        pyautogui.moveTo(tree_location[0] + tree_location[2] / 2, tree_location[1] + tree_location[3] / 2)
        pyautogui.click()
        stump_location = None
        while stump_location is None:
            stump_img = cv2.imread(stump_image)
            gray_stump_img = cv2.cvtColor(stump_img, cv2.COLOR_BGR2GRAY)
            screen =  pyautogui.screenshot()
            screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)
            res = cv2.matchTemplate(screen_gray, gray_stump_img, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= 0.8)
            if loc[0].size > 0:
                stump_location = (loc[1][0],loc[0][0],stump_img.shape[1],stump_img.shape[0])
                print("Found a stump!")
                break
    else:
        print(f"Tree location: {tree_location} -- GGWP")
        break