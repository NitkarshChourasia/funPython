import pyautogui
import time

# Add a short delay at the beginning to ensure the program starts smoothly
time.sleep(2)

# Constants for the coordinates to be used in the automation
CHROME_SEARCH_BAR_COORDS = (69, 750)        # Coordinates of Chrome's search bar
CHROME_COORDS = (478, 363)                 # Coordinates of the Chrome application icon
YOUTUBE_URL_BAR_COORDS = (177, 58)         # Coordinates of the URL bar in Chrome
SEARCH_BUTTON_COORDS = (458, 135)          # Coordinates of the search button in YouTube
VIDEO_SEARCH_COORDS = (763, 222)           # Coordinates of the first video search result
MINIMIZE_BUTTON_COORDS = (1253, 27)        # Coordinates of the minimize button in YouTube

# Function to automate the process of moving the cursor and clicking
def move_and_click(coords, duration=1):
    """Move the cursor to the specified coordinates and perform a mouse click.
    
    Parameters:
        coords (tuple): Tuple containing (x, y) coordinates to move the cursor to.
        duration (int, optional): Duration in seconds for the mouse movement and click. Default is 1 second.
    """
    pyautogui.moveTo(coords[0], coords[1], duration=duration)
    pyautogui.click(coords[0], coords[1], duration=duration)

# Function to automate typing into the search bar
def type_text(text):
    """Type the specified text at the current cursor position.
    
    Parameters:
        text (str): Text to be typed.
    """
    pyautogui.write(text)

# Function to add a short delay between actions
def short_delay(seconds):
    """Pause the program execution for the specified duration in seconds.
    
    Parameters:
        seconds (int): Duration in seconds to pause the program.
    """
    time.sleep(seconds)

def main():
    try:
        # Automate launching Chrome and searching for YouTube
        move_and_click(CHROME_SEARCH_BAR_COORDS)
        type_text('Chrome')
        move_and_click(CHROME_COORDS)

        # Type the YouTube URL and search
        move_and_click(YOUTUBE_URL_BAR_COORDS)
        type_text('https://www.youtube.com/')
        pyautogui.press('enter')

        # Search for a video and play it
        move_and_click(SEARCH_BUTTON_COORDS)
        type_text('perfect strangers')
        pyautogui.press('Enter')
        short_delay(3)  # Give some time for the search results to load
        move_and_click(VIDEO_SEARCH_COORDS)

        # Minimize the YouTube window
        move_and_click(MINIMIZE_BUTTON_COORDS)
        print("Automation completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
