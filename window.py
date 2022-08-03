from tkinter import *
import pyautogui
import os

#This function contains the screenshot logic through event handling
def take_screenshot():

	window_screen_posx = transparent_window.winfo_rootx() #Window X coordinate
	window_screen_posy = transparent_window.winfo_rooty() #Window Y coordinate
	window_screen_width = transparent_window.winfo_width() #Window width
	window_screen_height = transparent_window.winfo_height() #Window height

	path = os.getcwd() + "\\image.jpg"

	pyautogui.screenshot(path, region=(window_screen_posx, window_screen_posy, window_screen_width, window_screen_height))



#Create a window
window = Tk()

window.title("Press the F key to take screenshot")

#the window will have this dimension when the program starts
window.geometry("300x300")

button = Button(window, text="take screenshot", command=take_screenshot)
button.pack(pady=20)	


#This sentence make that the background become transparent
window.wm_attributes('-transparentcolor', '#add123')

transparent_window = Frame(window, width=1920, height=1080, bg="#add123")
transparent_window.pack(pady=30)


window.mainloop() #this sentence makes window show up
