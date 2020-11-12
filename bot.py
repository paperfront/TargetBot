import pyautogui
import time

PICKUP_IMAGE = 'images/pick_up.png'
CHECKOUT_1_IMAGE = 'images/checkout_1.png'
CHECKOUT_2_IMAGE = 'images/checkout_2.png'
DECLINE_COVERAGE_IMAGE = 'images/decline_coverage.png'
PLACE_ORDER_IMAGE = 'images/place_order.png'
SAFE_SPACE = (1000, 0)
CHROME_WINDOW = pyautogui.getWindowsWithTitle("Google Chrome")[0]

def get_input(input_name):
    correct = False
    while not correct:
        userInput = input("Enter your {} (no spaces): ".format(input_name))
        print("You entered {}".format(userInput))
        correct = input("Is this correct? (enter y/n): ") == 'y'
        print()
    return userInput

def maximize_chrome():
    print("Maximizing Chrome in")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    CHROME_WINDOW.activate()
    CHROME_WINDOW.maximize()

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

def find_element(image_name, breakOnUnableToFind=False, countLimit=100):
    found = False
    count = 0
    while not found:
        if count > countLimit:
            print("Failed to find button for {}".format(image_name[:-3]))
            if breakOnUnableToFind:
                exit()
            return None
        location = pyautogui.locateOnScreen(image_name)
        found = location is not None
        time.sleep(0.1)
        count += 1
    return location

def clear_mouse():
    pyautogui.moveTo(SAFE_SPACE, duration=0.1)

def main():
    print(CHROME_WINDOW)
    print("-----STARTING BOT-----")
    ccSecurityCode = get_input('security code')
    refreshTime = int(input("Enter how often you want to refresh the page (in seconds): "))
    print()
    print()
    maximize_chrome()
    while True:
        clear_mouse()
        pick_up_location = find_element(PICKUP_IMAGE)
        if not pick_up_location:
            time.sleep(refreshTime)
            refresh_page()
            continue
        else:
            print("PLAY STATION FOUND")
            pyautogui.click(pick_up_location)
            print("DECLINING WARRANTY")
            decline_coverage = find_element(DECLINE_COVERAGE_IMAGE, breakOnUnableToFind=False, countLimit=50)
            pyautogui.click(decline_coverage)
            clear_mouse()
            print("CHECKOUT PART 1")
            checkout_1 = find_element(CHECKOUT_1_IMAGE, breakOnUnableToFind=True)
            pyautogui.click(checkout_1)
            clear_mouse()
            print("CHECKOUT PART 2")
            checkout_2 = find_element(CHECKOUT_2_IMAGE, breakOnUnableToFind=True)
            pyautogui.click(checkout_2)
            clear_mouse()
            place_order = find_element(PLACE_ORDER_IMAGE, breakOnUnableToFind=True)
            print("ENTERING SECURITY CODE")
            pyautogui.write(ccSecurityCode, interval=0.1)
            time.sleep(0.2)
            place_order = find_element(PLACE_ORDER_IMAGE, breakOnUnableToFind=True)
            pyautogui.click(place_order)
            clear_mouse()
            print("PLACED ORDER")
            exit()


main()
