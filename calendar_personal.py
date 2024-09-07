import pygetwindow as gw
import pyautogui
import subprocess
import time


def get_calendar():
    subprocess.Popen(['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', '--new-window', 'https://calendar.google.com/calendar/u/0/r?pli=1'])
    time.sleep(2)  # Wait for the browser to open and load the page

    # Find the browser window (example uses "weather" in the title)
    calendar_window = None
    for window in gw.getWindowsWithTitle('calendar'):
        calendar_window = window
        break

    if calendar_window:    
        # Define desired position and size
        desired_position = (800, -100)
        desired_size = (1180, 640)

        # Move and resize the window using pygetwindow
        def move_and_resize_window(window):
            window.restore()  # Make sure the window is not minimized or maximized
            window.moveTo(*desired_position)
            window.resizeTo(*desired_size)
            time.sleep(1)


        # Check if the window is in the correct position and size
        def is_window_correct(window):
            return (window.left == desired_position[0] and
                    window.top == desired_position[1] and
                    window.width == desired_size[0] and
                    window.height == desired_size[1])

        attempts = 5
        for attempt in range(attempts):
            print("CALENDAR: ")
            move_and_resize_window(calendar_window)
            if is_window_correct(calendar_window):
                print(f"Attempt {attempt+1}: Window positioned and resized successfully.")
                break
            else:
                print(f"Attempt {attempt+1}: Window not in the correct position or size, retrying...")
                time.sleep(2)  # Wait before retrying
        else:
            print("Failed to position and resize the window after multiple attempts.")

            # Fallback: Use pyautogui to drag the window to the desired position
            print("Using pyautogui as fallback to move and resize the window.")
            calendar_window.activate()
            pyautogui.moveTo(calendar_window.left + 10, calendar_window.top + 10)
            pyautogui.dragTo(desired_position[0], desired_position[1], duration=1)  # Drag to the desired position
            pyautogui.hotkey('alt', 'space')
            pyautogui.press('s')  # Resize window
            pyautogui.dragTo(desired_size[0], desired_size[1], duration=1)
            time.sleep(1)

    else:
        print("Calendar window not found.")


    return "Stuff on Tuesday"

# Testing
if __name__ == "__main__":
    print(get_calendar())