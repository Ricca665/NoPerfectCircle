import pyautogui
import time

def get_mouse_coordinates():
    try:
        while True:
            x, y = pyautogui.position()
            print(f'Mouse coordinates: x = {x}, y = {y}')
            time.sleep(1)  # Adjust the delay to control how often coordinates are printed

    except KeyboardInterrupt:
        print('Program terminated by user.')

if __name__ == "__main__":
    get_mouse_coordinates()

