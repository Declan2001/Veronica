import webbrowser
import pygetwindow as gw
import pyautogui
import time

def get_stocks():
    webbrowser.open("https://weather.com/weather/hourbyhour/l/Philadelphia%2BPA?canonicalCityId=aa0f46aff5c7ee96eb5fdea10c53c77c9578eb071854d7f04ae0a7aa517772ab")
    time.sleep(4)  # Wait for the browser to open and load the page

    # Find the browser window (example uses "weather" in the title)
    stock_window = None
    for window in gw.getWindowsWithTitle('robinhood'):
        stock_window = window
        break

    if stock_window:
        # Move and resize the window
        stock_window.moveTo(900, 540)
        stock_window.resizeTo(540, 540)
        time.sleep(1)
        pyautogui.scroll(-230)  # Negative value scrolls down
    
    return "Your rich!"