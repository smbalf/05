import os
from dotenv import load_dotenv
import pyautogui
from pywinauto import Application
from pynput import keyboard


load_dotenv()
TITLE=os.getenv("TITLE")
SCREEN_LEFT=578
SCREEN_RIGHT=290
SCREEN_WIDTH=520
SCREEN_HEIGHT=345
SCREEN_REGION=(SCREEN_LEFT,SCREEN_RIGHT,SCREEN_WIDTH, SCREEN_HEIGHT)

app = Application().connect(title=TITLE)
app.top_window().set_focus()

x = 1

def on_press(key):
    global x
    try:
        if key.char == 's':
            screenshot = pyautogui.screenshot(region=SCREEN_REGION)
            # COMMENT OUT ONE OF THE TWO BELOW
            #screenshot.save(f'training_images/positive/pos-{x}.png') 
            screenshot.save(f'training_images/negative/neg-{x}.png')
            print(f'Screenie #{x} saved')
            x += 1
        elif key.char == 'q':
            quit()
    except AttributeError:
        pass

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()