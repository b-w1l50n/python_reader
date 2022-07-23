# pyautogui numpy opencv for screenshot
# pytesseract for OCR
# gtts for text-to-speech
# os sys for basic stuff
import sys

def screenshot():
    sys.exit("This is just a placeholder!")

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
            print(f"Are you sure {num} is a valid number? Please select either '1' or '2'.\n")

if __name__ == '__main__':
    main()
