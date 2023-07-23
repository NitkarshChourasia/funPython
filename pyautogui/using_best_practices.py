import pyautogui


def move_cursor_to_center():
    screen_width, screen_height = pyautogui.size()
    x, y = screen_width / 2, screen_height / 2
    pyautogui.moveTo(x, y)

if __name__ == "__main__":
    move_cursor_to_center()



import pyautogui

def perform_mouse_click():
    pyautogui.click()

if __name__ == "__main__":
    perform_mouse_click()



import pyautogui

def type_hello_world():
    text_to_type = "Hello, World!"
    pyautogui.typewrite(text_to_type)

if __name__ == "__main__":
    type_hello_world()
