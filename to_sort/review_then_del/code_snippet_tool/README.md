# Code Snippet Screenshot Tool

This Python script allows you to capture a code snippet screenshot from your preferred Integrated Development Environment (IDE) using the PyAutoGUI library. The script waits for 3 seconds to give you enough time to switch to your IDE, captures the screenshot, and saves it as an image file. It provides an option to specify the output location where the screenshot will be saved and ensures that it does not overwrite any existing files with the same name.

## Required Libraries
- PyAutoGUI
- Time
- OS

## How to Use

1. Install the required libraries using the following command:
   ```
   pip install pyautogui
   ```

2. Copy and paste the provided code into a Python script file (e.g., `code_snippet_tool.py`).

3. In the `main()` function, set the `output_location` variable to the desired output directory where you want to save the screenshot.

4. Run the script using the following command:
   ```
   python code_snippet_tool.py
   ```

5. Switch to your preferred IDE within the 3-second waiting time.

6. After the script successfully captures the screenshot, it will display a message indicating the name of the saved screenshot and the output location.

7. If a file with the same name (`code_snippet.png`) already exists in the output directory, the script will append a number to the file name to avoid overwriting existing files (e.g., `code_snippet_1.png`, `code_snippet_2.png`, and so on).

## Program Code

```python
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
```

## Repository Name Suggestions

1. code-snippet-screenshot-tool
2. IDE-screenshot-capture
3. Python-Code-Snippet-Capture


# Also host it to this website.

https://github.com/josharsh/100LinesOfCode

## Following all the guidelines of it.


# Also, make a documentation site for this project, too.