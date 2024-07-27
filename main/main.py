import tkinter as tk
from tkinter import ttk
from tkinter import font
root = tk.Tk()
root.minsize(100, 350)
root["background"] = "#222222"
style = ttk.Style()


home_frame = tk.Frame(root)
home_frame.pack(expand=True)

home_frame["background"] = "#222222"

homeskool_title = tk.Label(home_frame, text="HomeSkool", font=("Poor Richard", 80, "bold"))
homeskool_title.grid(row=0, column=0, padx=40, pady=(40, 100))

homeskool_title["background"] = "#222222"
homeskool_title["foreground"] = "white"

style.configure("home_page_button_style.TButton", font=("Times New Roman", 30, "bold"), foreground="#222222", relief="flat")
style.configure("help_button_style.TButton", font=("Times New Roman", 14, "bold"), foreground="#222222")

login_button = ttk.Button(home_frame, text="Log In", style="home_page_button_style.TButton")
login_button.grid(row=1, column=0, ipadx=30, ipady=10)

signup_button = ttk.Button(home_frame, text="Sign Up", style="home_page_button_style.TButton")
signup_button.grid(row=2, column=0, ipadx=30, ipady=10, pady=(20, 5))

help_button = ttk.Button(home_frame, text="Help", style="help_button_style.TButton")
help_button.grid(row=3, column=0, pady=(40,10))

root.mainloop()
