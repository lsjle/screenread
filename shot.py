from pynput import mouse
from PIL import ImageGrab
import matplotlib as mpl
import time
import matplotlib.pyplot as plt
def on_click(x, y, button, pressed):
    global x1, y1, x2, y2

    if pressed:
        # Capture the starting coordinates on mouse press
        x1, y1 = x, y
    else:
        # Capture the ending coordinates on mouse release
        x2, y2 = x, y
        return False  # Stop listener


def take_screenshot(output_path):
    # Take a screenshot and save it to the specified output path
    screenshot = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    width, height = screenshot.size
    # Set the figure size to match the image dimensions
    fig=plt.subplots(figsize=(width / 100, height / 100), dpi=100)
    # Turn off the toolbar at the bottom
    imgplot = plt.imshow(screenshot,aspect='equal')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.axis('off')  # Turn off axis labels
    plt.show()
def main():
    # Specify the path for the screenshot
    screenshot_path = "/path/to/screenshot.png"
    
    # Start the mouse listener
    with mouse.Listener(on_click=on_click,suppress=True) as listener:
        print("Click and drag to select a region for the screenshot.")
        listener.join()

    # Take a screenshot
    take_screenshot(screenshot_path)

    # Optional: Wait for a few seconds before the script exits (adjust as needed)

if __name__ == "__main__":
    mpl.rcParams['toolbar'] = 'None'
    main()

