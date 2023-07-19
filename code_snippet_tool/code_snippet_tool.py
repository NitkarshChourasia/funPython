# Required Libraries
import pyautogui
import time
import os

# Function to capture the code snippet screenshot
def capture_screenshot():
    time.sleep(3)  # Give some time to switch to the IDE
    screenshot = pyautogui.screenshot()
    return screenshot

# Function to save the screenshot as an image
def save_screenshot(image, output_location):
    # Check if the file name already exists in the output directory
    file_name = "code_snippet.png"
    count = 1
    while os.path.exists(os.path.join(output_location, file_name)):
        file_name = f"code_snippet_{count}.png"
        count += 1

    image.save(os.path.join(output_location, file_name))
    return file_name

# Main Function
def main():
    try:
        # Specify the output directory where you want to save the screenshot
        output_location = "path/to/output/directory"

        # Capture code snippet screenshot
        screenshot = capture_screenshot()

        # Save the screenshot as an image
        saved_file_name = save_screenshot(screenshot, output_location)

        print(f"Code snippet screenshot captured successfully and saved as '{saved_file_name}' in '{output_location}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
