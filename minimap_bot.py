import pyautogui
from pywinauto import Application
import cv2
import numpy as np
import os
from dotenv import load_dotenv

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
os.system('cls')
tree_img = cv2.imread(TREE_IMAGE)
result = cv2.matchTemplate(minimap, tree_img, cv2.TM_CCOEFF_NORMED)
threshold = 0.65

loc = np.where(result >= threshold)
trees_found = loc[0].size
if trees_found > 0:
    print(f'Number of trees found: {trees_found}')
    if trees_found <= 30:
        for i in range(loc[0].size):
            x = loc[1][i]
            y = loc[0][i]
            print(f"Tree found at: ({x}, {y})")
            cv2.putText(minimap, ".", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (125, 246, 55), 2)
            cv2.imwrite(f'output_images/trees_found.png', minimap)
else:
    print("No trees found.")
