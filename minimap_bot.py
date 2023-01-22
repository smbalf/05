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

TREE_IMAGE = "images/minimap_tree.png"

app = Application().connect(title=TITLE)
app.top_window().set_focus()

minimap = pyautogui.screenshot(region=REGION)
minimap.save("output_images/current_minimap.png")
minimap = np.array(minimap)

grey_minimap = cv2.cvtColor(minimap, cv2.COLOR_RGB2GRAY)

tree_img = cv2.imread(TREE_IMAGE)
grey_tree_img = cv2.cvtColor(tree_img, cv2.COLOR_BGR2GRAY)

grey_result = cv2.matchTemplate(grey_minimap, grey_tree_img, cv2.TM_CCOEFF_NORMED)


os.system('cls')

grey_threshold = 0.8
grey_loc = np.where(grey_result >= grey_threshold)
grey_trees_found = grey_loc[0].size
if grey_trees_found > 0:
    print(f'Number of trees found: {grey_trees_found}')
    if grey_trees_found <= 30:
        for i in range(grey_loc[0].size):
            x = grey_loc[1][i]
            y = grey_loc[0][i]
            cv2.putText(grey_minimap, ".", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (125, 246, 55), 2)
            cv2.imwrite(f'output_images/grey_trees_found.png', grey_minimap)

else:
    print("No trees found.")
    cv2.imwrite(f'output_images/grey_trees_found.png', grey_minimap)