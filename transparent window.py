from tkinter import *
import pyautogui

#Create a window
window = Tk()

#Set a background color like a chroma
window.config(bg = '#add123')

#This sentence make that the background become transparent
window.wm_attributes('-transparentcolor', '#add123')

#This function contains the screenshot logic through event handling
def key_pressed(event):
	
	#if you press the F key, it will take the screenshot where the window is
	if event.char == "f":
		window_screen_posx = window.winfo_rootx() #Window X coordinate
		window_screen_posy = window.winfo_rooty() #Window Y coordinate
		window_screen_width =window.winfo_width() #Window width
		window_screen_height = window.winfo_height() #Window height
		
		pyautogui.screenshot("image.jpg", region=(window_screen_posx, window_screen_posy, window_screen_width, window_screen_height))


#This sentence assigns the previous function to a keyboard event, in this case, the F key
window.bind("<Key>", key_pressed)

window.mainloop() #this sentence makes window show up
