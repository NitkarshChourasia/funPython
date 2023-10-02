# Required Libraries
import pyautogui
import time

# Function to capture the code snippet screenshot
def capture_screenshot():
    time.sleep(5)  # Give some time to switch to the IDE
    screenshot = pyautogui.screenshot()
    return screenshot

# Function to save the screenshot as an image
def save_screenshot(image):
    image.save('code_snippet.png')

# Main Function
def main():
    # Capture code snippet screenshot
    screenshot = capture_screenshot()

    # Save the screenshot as an image
    save_screenshot(screenshot)

if __name__ == "__main__":
    main()
