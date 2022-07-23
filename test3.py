# pyautogui numpy opencv for screenshot
# pytesseract for OCR
# gtts for text-to-speech
# os sys for basic stuff
import sys
import time
import pyautogui

def screenshot():
    print("You have 10 seconds to focus your interest text")

    time.sleep(10)

    # Screenshot will be saved as "image.jpg" in the same directory as the script
    pyautogui.screenshot("image.jpg")

def exit():
    sys.exit("Thanks for using our program!")

def main():
    num = input("Please make a selection:\n[1]. Take a Screenshot. \n[2]. Exit.\n")
    match num.split():
        case ["1"]:
            screenshot()
        case ["2"]:
            exit()
        case _:
            print(f"Are you sure {num} is a valid number? Try again. \n")
    
if __name__ == '__main__':
    main()
