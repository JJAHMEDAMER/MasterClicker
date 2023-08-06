import pyautogui
from time import sleep
import customtkinter as ctk

count_down_time = 5


def click():
    if btn_text.get() == "Start":
        window.attributes("-topmost", True)
        btn_text.set("Stop")
        count_down()
    else:
        cancel()


def clickLoop():
    pyautogui.click()
    global infinite_loop
    infinite_loop = window.after(10, clickLoop)
    print("hi")


def count_down():
    global count_down_time
    if count_down_time >= 0:
        sleep(1)
        print((counter._text))
        counter.configure(text=f"Count Down: {count_down_time}")
        count_down_time = count_down_time - 1
        global tk_count_down
        tk_count_down = window.after(1000, count_down)
    else:
        clickLoop()


def esc_button(event):
    if event.keysym == "Escape" or event.type == "9":
        cancel()


def cancel():
    global count_down_time
    count_down_time = 5  # reset count_down_time
    window.attributes("-topmost", False)
    btn_text.set("Start")
    window.after_cancel(infinite_loop)
    window.after_cancel(tk_count_down)
    print("focus")


window = ctk.CTk()
window.title("Click Master")
window.geometry("500x150")
window.bind("<Key>", esc_button)
window.bind("<FocusIn>", esc_button)

title = ctk.CTkLabel(master=window, text="Welcome to click master")
title.pack()

btn_text = ctk.StringVar()
button = ctk.CTkButton(master=window, textvariable=btn_text, command=click)
btn_text.set("Start")
button.pack()

counter = ctk.CTkLabel(master=window, text="")
counter.pack()

window.lift()
window.mainloop()
