import pyautogui
from time import sleep
import customtkinter as ctk


def click():
    print("clicked")


window = ctk.CTk()
window.title("Click Master")
window.geometry("500x150")

title = ctk.CTkLabel(master=window, text="Welcome to click master")
title.pack()

button = ctk.CTkButton(master=window, text="Start", command=click)
button.pack()

window.mainloop()
# sleep(5)
# while True:
#     pyautogui.click()
