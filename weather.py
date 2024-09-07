import pygetwindow as gw
import pyautogui
import subprocess
import time


def get_weather():
    subprocess.Popen(['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', '--new-window', 'https://weather.com/weather/hourbyhour/l/Philadelphia%2BPA?canonicalCityId=aa0f46aff5c7ee96eb5fdea10c53c77c9578eb071854d7f04ae0a7aa517772ab'])
    time.sleep(3)  # Wait for the browser to open and load the page

    # Find the browser window (example uses "weather" in the title)
    weather_window = None
    for window in gw.getWindowsWithTitle('Philadelphia'):
        weather_window = window
        break

    if weather_window:
        # Define desired position and size
        desired_position = (-10, 0)
        desired_size = (1280, 1080)

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

        # Attempt to move and resize until successful
        attempts = 5
        for attempt in range(attempts):
            print("WEATHER: ")
            move_and_resize_window(weather_window)
            if is_window_correct(weather_window):
                print(f"Attempt {attempt+1}: Window positioned and resized successfully.")
                break
            else:
                print(f"Attempt {attempt+1}: Window not in the correct position or size, retrying...")
                time.sleep(2)  # Wait before retrying
        else:
            print("Failed to position and resize the window after multiple attempts.")

            # Fallback: Use pyautogui to drag the window to the desired position
            print("Using pyautogui as fallback to move and resize the window.")
            weather_window.activate()
            pyautogui.moveTo(weather_window.left + 10, weather_window.top + 10)
            pyautogui.dragTo(desired_position[0], desired_position[1], duration=1)  # Drag to the desired position
            pyautogui.hotkey('alt', 'space')
            pyautogui.press('s')  # Resize window
            pyautogui.dragTo(desired_size[0], desired_size[1], duration=1)
            time.sleep(1)

        # Scroll down the page
        try:
            weather_window.activate()  # Make sure the window is active
            time.sleep(1)
            pyautogui.scroll(-230)  # Negative value scrolls down
            print("Scrolled down the page.")
        except Exception as e:
            print(f"Error activating or scrolling the window: {e}")

    else:
        print("Weather window not found.")

    return "Weather!"

# Test the function
if __name__ == "__main__":
    result = get_weather()
    print(result)
