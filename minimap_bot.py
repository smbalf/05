import os
from dotenv import load_dotenv
import pyautogui
from pywinauto import Application
import cv2
import numpy as np


load_dotenv()
TITLE=os.getenv("TITLE")
LEFT=1150
RIGHT=300
WIDTH=150
HEIGHT=150
REGION=(LEFT,RIGHT,WIDTH,HEIGHT)

app = Application().connect(title=TITLE)
app.top_window().set_focus()

minimap_tree_png = "images/minimap_tree.png"
THRESHOLD = 0.6

def get_images(minimap_tree_png):
    minimap = pyautogui.screenshot(region=REGION)
    minimap.save("output_images/current_minimap.png")
    minimap = np.array(minimap)

    tree_img = cv2.imread(minimap_tree_png)
    grey_tree_img = cv2.cvtColor(tree_img, cv2.COLOR_BGR2GRAY)
    grey_minimap = cv2.cvtColor(minimap, cv2.COLOR_RGB2GRAY)
    get_result(grey_minimap, grey_tree_img)

def get_result(grey_minimap, grey_tree_img):
    result = cv2.matchTemplate(grey_minimap, grey_tree_img, cv2.TM_CCOEFF_NORMED)
    find_trees(result, grey_minimap)

def find_trees(result, grey_minimap):
    threshold = THRESHOLD
    loc = np.where(result >= threshold)
    trees_found = loc[0].size
    os.system('cls')

    if trees_found:
        distances = []
        print(f'Number of trees found: {trees_found}')
        if trees_found <= 30:
            for i in range(loc[0].size):
                x = loc[1][i]
                y = loc[0][i]
                distance = ((x - WIDTH/2) ** 2 + (y - HEIGHT/2) ** 2) ** 0.5
                distances.append(distance)
                #cv2.putText(grey_minimap, ".", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                #cv2.imwrite(f'output_images/trees_found.png', grey_minimap)
        find_nearest_tree(distances, loc, grey_minimap)

    else:
        print("No trees found.")

def find_nearest_tree(distance_list, loc, grey_minimap):
    distance = [int(x) for x in distance_list]
    nearest_tree = min(distance)
    tree_index = distance.index(nearest_tree)
    x_nearest = loc[1][tree_index]
    y_nearest = loc[0][tree_index]
    print(f'Nearest tree: ({x_nearest}, {y_nearest}) - Dist: {nearest_tree}')
    #cv2.putText(grey_minimap, ".", (x_nearest, y_nearest), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 2)
    #cv2.imwrite(f'output_images/trees_found.png', grey_minimap)


get_images(minimap_tree_png)