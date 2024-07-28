import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import simpledialog
import toml
from tkinter import messagebox
from datetime import date

root = tk.Tk()
root.minsize(600, 500)
root["background"] = "#222222"
style = ttk.Style()

# Variables
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_address_var = tk.StringVar()
password_var = tk.StringVar()


# Set Variables
first_name_var.set("Lloyd")
last_name_var.set("Andersen")
email_address_var.set("lloydandersen@gmail.com")
password_var.set("dang")
# App utility functions


# App run bool
reading_bool_var = tk.BooleanVar()
writing_bool_var = tk.BooleanVar()
math_bool_var = tk.BooleanVar()
science_bool_var = tk.BooleanVar()
social_studies_bool_var = tk.BooleanVar()
fitness_bool_var = tk.BooleanVar()
other_skill_bool_var = tk.BooleanVar()

def clear_root_frame():
    list = root.winfo_children()
    for children in list:
        children.pack_forget()


def create_skills_button_frame(parent):
    skills_button_frame = tk.Frame(parent)
    skills_button_frame.grid(row=1, column=1, padx=15, pady=15)
    skills_button_frame["background"] = "#222222"


    reading_list_button = tk.Button(skills_button_frame, text="Reading", font=("Times New Roman", 18), height=5, width=10)
    reading_list_button.grid(row=0, column=0, sticky="swen", padx=5, pady=5)

    writing_prompt_button = tk.Button(skills_button_frame, text="Writing", font=("Times New Roman", 18), height=5, width=10)
    writing_prompt_button.grid(row=0, column=1, sticky="swen", padx=5, pady=5)

    math_button = tk.Button(skills_button_frame, text="Math", font=("Times New Roman", 18), height=5, width=10)
    math_button.grid(row=0, column=2, sticky="swen", padx=5, pady=5)

    science_button = tk.Button(skills_button_frame, text="Science", font=("Times New Roman", 18), height=5, width=10)
    science_button.grid(row=1, column=0, sticky="swen", padx=5, pady=5)

    social_studies_button = tk.Button(skills_button_frame, text="Social\nStudies", font=("Times New Roman", 18), height=5, width=10)
    social_studies_button.grid(row=1, column=1, sticky="swen", padx=5, pady=5)

    arts_button = tk.Button(skills_button_frame, text="Arts", font=("Times New Roman", 18), height=5, width=10)
    arts_button.grid(row=1, column=2, sticky="swen", padx=5, pady=5)

    other_skills_button = tk.Button(skills_button_frame, text="Other", font=("Times New Roman", 18), height=5, width=10)
    other_skills_button.grid(row=2, column=1, sticky="swen", padx=5, pady=5)


def open_skill_page(*args):
    clear_root_frame()
    skill_page.pack(side="top", fill="both")
    create_side_menu(skill_page)
    skill_page["background"] = "#222222"
    create_skills_button_frame(skill_page)
    skill_page_title = tk.Label(skill_page, text="Skills", foreground="white", background="#222222", font=("Poor Richard", 30))
    skill_page_title.grid(row=0, column=1)



# Control
def open_help_page():
    clear_root_frame()
    help_frame.pack(expand=True)
    help_frame["background"] = "#222222"

def back_to_home():
    clear_root_frame()
    home_frame.pack(expand=True)

def open_login_page():
    clear_root_frame()
    login_frame.pack(expand=True)
    login_frame["background"] = "#222222"


def open_signup_page():
    list = root.winfo_children()
    for children in list:
        children.pack_forget()
    signup_frame.pack(expand=True)
    signup_frame["background"] = "#222222"


def create_account():
    account_file = open('homeskool_accounts.toml', 'a')

    account = {
        f"{email_address_var.get()}" :{
            "first_name" : f"{first_name_var.get()}",
            "last_name" : f"{last_name_var.get()}",
            "email_address" : f"{email_address_var.get()}",
            "password" : f"{password_var.get()}"
        }
    }
    toml.dump(account, account_file)
    first_name_var.set("")
    last_name_var.set("")
    email_address_var.set("")
    password_var.set("")
    account_file.close()
    open_login_page()


def read_account():
    accounts_file = open("homeskool_accounts.toml", "r")
    account = toml.load(accounts_file)[email_address_var.get()]
    first_name_var.set(account["first_name"])
    last_name_var.set(account["last_name"])




def start_app(*args):
    read_account()
    clear_root_frame()
    create_side_menu(start_frame)
    start_frame.pack(side="top", fill="both")
    start_frame["background"] = "#222222"
    start_frame.grid_columnconfigure(1, weight=10)
    start_frame.grid_columnconfigure(2, weight=1)
    start_frame_title = ttk.Label(start_frame, text=f"Welcome, {first_name_var.get()}", style="top_page_style.TLabel")
    start_frame_title.grid(row=0, column=1, sticky="ne")
    start_frame_date_label = ttk.Label(start_frame, text=f"{date.today()}", justify="right", style="top_page_style.TLabel")
    start_frame_date_label.grid(row=0, column=2, padx=(0, 0), sticky="n")
    create_current_work_frame()



def login_account():
    try:
        email_address = email_address_var.get()
        account_file = open('homeskool_accounts.toml', 'r')
        account = toml.load(account_file)[f"{email_address}"]
        password = account['password']
        if password_var.get() == password:
            password_var.set("")
            start_app()
        elif password_var.get() == "":
            password_var.set("")
            tk.messagebox.showinfo("Password", "Please Enter Password!")
        else:
            password_var.set("")
            tk.messagebox.showinfo("Password", "Wrong Password!")
        account_file.close()
    except KeyError:
        if email_address_var.get() == "":
            tk.messagebox.showinfo("Email!", "Please Enter an Email!!")
        else:
            tk.messagebox.showinfo("Email!", "Email does not exist!")



def create_new_password(*args):
    answer = tk.simpledialog.askstring("New Password", "What is your new password?")


# Home Page
home_frame = tk.Frame(root)
home_frame.pack(expand=True)

home_frame["background"] = "#222222"

homeskool_title = tk.Label(home_frame, text="HomeSkool", font=("Poor Richard", 80, "bold"))
homeskool_title.grid(row=0, column=0, padx=40, pady=(40, 40))

homeskool_title["background"] = "#222222"
homeskool_title["foreground"] = "#6699cc"

style.configure("home_page_button_style.TButton", font=("Times New Roman", 30, "bold"), foreground="#222222", relief="flat")
style.configure("help_button_style.TButton", font=("Times New Roman", 14, "bold"), foreground="#222222")
style.configure("help_content_style.TLabel", font=("Times New Roman", 14), foreground="white", background="#222222")
style.configure("help_title_style.TLabel", font=("Poor Richard", 50, "bold"), foreground="#6699cc", background="#222222")
style.configure("home_page_button_style.TLabel", font=("Times New Roman", 30, "bold"), foreground="#222222", relief="flat")
style.configure("login_label_style.TLabel", font=("Times New Roman", 18), foreground="white", background="#222222")
style.configure("login_entry_style.TEntry", foreground="#222222")
style.configure("action_buttons_style.TButton", font=("Times New Roman", 14, "bold"), foreground="#222222")
style.configure("forgot_password_style.TLabel", font=("Times New Roman", 14), foreground="#6699cc", background="#222222")
style.configure("top_page_style.TLabel", font=("Times New Roman", 14), foreground="white", background="#222222")
style.configure("Side_menu_style.TLabel", font=("Poor Richard", 30), foreground="#6699cc", background="#222222")
style.configure("Side_menu_button.TLabel",font=("Times New Roman", 20), foreground="white", background="#222222")
style.configure("Side_menu_exit_button.TLabel",font=("Times New Roman", 20), foreground="#f10809", background="#222222")
style.configure("current_work_label.TLabel", font=("Poor Richard", 40), foreground="#222222", background="white")
style.configure("current_work_check_box.TCheckbutton", font=("Times New Roman", 20), foreground="#222222", background="white")

login_button = ttk.Button(home_frame, text="Log In", style="home_page_button_style.TButton", command=open_login_page)
login_button.grid(row=1, column=0, ipadx=30, ipady=10)

signup_button = ttk.Button(home_frame, text="Sign Up", style="home_page_button_style.TButton", command=open_signup_page)
signup_button.grid(row=2, column=0, ipadx=30, ipady=10, pady=(20, 5))

help_button = ttk.Button(home_frame, text="Help", style="help_button_style.TButton", command=open_help_page)
help_button.grid(row=3, column=0, pady=(40,10))

# Help Page

help_frame = tk.Frame(root)
help_page_title = ttk.Label(help_frame, text="Help",style="help_title_style.TLabel")
help_page_title.grid(row=0, column=0, pady=(0, 30), padx=50, sticky="n")

help_page_content = ttk.Label(help_frame,
                              text="""HomeSkool is an education assistant for parents, guardians and other educators.
                              \n\nHomeSkool is free and open source under the MIT License.
                              \n\nHomeSkool was created by Lloyd Andersen in 2024.""",
                              style="help_content_style.TLabel")
help_page_content.grid(row=1, column=0, padx=50)

help_to_home_button = ttk.Button(help_frame, text="back", command=back_to_home, style="action_buttons_style.TButton")
help_to_home_button.grid(row=2, column=0, sticky="s", pady=30)


# Signup Page
signup_frame = tk.Frame(root)

signup_page_title = ttk.Label(signup_frame, text="Signup", style="help_title_style.TLabel")
signup_page_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

first_name_label = ttk.Label(signup_frame, text="First Name", style="login_label_style.TLabel")
first_name_label.grid(row=1, column=0, padx=(0, 15), pady=5)
first_name_entry = ttk.Entry(signup_frame, textvariable=first_name_var, justify="center",
                             style="login_entry_style.TEntry", font=("Times New Roman", 14), width=30)

first_name_entry.grid(row=1, column=1, pady=5)

last_name_label = ttk.Label(signup_frame, text="Last Name", style="login_label_style.TLabel")
last_name_label.grid(row=2, column=0, padx=(0, 15), pady=5)
last_name_entry = ttk.Entry(signup_frame, textvariable=last_name_var, justify="center",
                             style="login_entry_style.TEntry", font=("Times New Roman", 14), width=30)

last_name_entry.grid(row=2, column=1, pady=5)

signup_email_label = ttk.Label(signup_frame, text="Email", style="login_label_style.TLabel")
signup_email_label.grid(row=3, column=0, padx=(0, 15), pady=5)
signup_email_entry = ttk.Entry(signup_frame, textvariable=email_address_var, justify="center",
                             style="login_entry_style.TEntry", font=("Times New Roman", 14), width=30)

signup_email_entry.grid(row=3, column=1, pady=5)

signup_password_label = ttk.Label(signup_frame, text="Password", style="login_label_style.TLabel")
signup_password_label.grid(row=4, column=0, padx=(0, 15), pady=5)
signup_password_entry = ttk.Entry(signup_frame, textvariable=password_var, justify="center",
                             style="login_entry_style.TEntry", font=("Times New Roman", 14), show='*', width=30)

signup_password_entry.grid(row=4, column=1, pady=5)



signup_to_home_button = ttk.Button(signup_frame, text="back", command=back_to_home, style="action_buttons_style.TButton")
signup_to_home_button.grid(row=5, column=0, sticky="w", pady=30)

create_account_button = ttk.Button(signup_frame, text="Signup", style="action_buttons_style.TButton",
                                   command=create_account)
create_account_button.grid(row=5, column=1, sticky="swen", pady=30)

# Login Page
login_frame = tk.Frame(root)


login_page_title = ttk.Label(login_frame, text="Login", style="help_title_style.TLabel")
login_page_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

login_email_label = ttk.Label(login_frame, text="Email", style="login_label_style.TLabel")
login_email_label.grid(row=1, column=0, padx=(0, 15), pady=5)
login_email_entry = ttk.Entry(login_frame, textvariable=email_address_var, justify="center",
                             style="login_entry_style.TEntry", font=("Times New Roman", 14), width=30)

login_email_entry.grid(row=1, column=1, pady=5)

login_password_label = ttk.Label(login_frame, text="Password", style="login_label_style.TLabel")
login_password_label.grid(row=2, column=0, padx=(0, 15), pady=5)
login_password_entry = ttk.Entry(login_frame, textvariable=password_var, justify="center",
                             style="login_entry_style.TEntry", font=("Times New Roman", 14), show='*', width=30)

login_password_entry.grid(row=2, column=1, pady=5)


login_to_home_button = ttk.Button(login_frame, text="back", command=back_to_home, style="action_buttons_style.TButton")
login_to_home_button.grid(row=3, column=0, sticky="w", pady=30)

login_account_button = ttk.Button(login_frame, text="Login", style="action_buttons_style.TButton",
                                   command=login_account)
login_account_button.grid(row=3, column=1, sticky="swen", pady=30, padx=(5, 0))

forgot_password_label = ttk.Label(login_frame, text="Forgot Password?", style="forgot_password_style.TLabel")
forgot_password_label.grid(row=4, column=0, columnspan=2)
forgot_password_label.bind("<Button-1>", create_new_password)



def open_work_page(*args):
    clear_root_frame()
    work_page.pack(side="top", fill="both")
    create_side_menu(work_page)
    work_page["background"] = "#222222"


# Work Frame
work_page = tk.Frame(root)

grades_page = tk.Frame(root)

# start frame
start_frame = tk.Frame(root)

def create_side_menu(parent):
    side_menu = tk.Frame(parent)
    side_menu.grid(row=0, column=0, rowspan=2, sticky="n")
    side_menu["background"] = "#222222"
    side_menu_title = ttk.Label(side_menu, text="HomeSkool", style="Side_menu_style.TLabel")
    side_menu_title.grid(row=0, column=0)

    side_menu_overview_button = ttk.Label(side_menu, text="Overview", style="Side_menu_button.TLabel")
    side_menu_overview_button.grid(row=1, column=0, pady=(15,5))

    side_menu_overview_button.bind("<Button-1>", start_app)

    side_menu_work_button = ttk.Label(side_menu, text="Work", style="Side_menu_button.TLabel")
    side_menu_work_button.grid(row=2, column=0, pady=5)
    side_menu_work_button.bind("<Button-1>", open_work_page)

    side_menu_grades_button = ttk.Label(side_menu, text="Grades", style="Side_menu_button.TLabel")
    side_menu_grades_button.grid(row=3, column=0, pady=5)

    side_menu_skill_tree_button = ttk.Label(side_menu, text="Skills", style="Side_menu_button.TLabel")
    side_menu_skill_tree_button.grid(row=4, column=0, pady=5)
    side_menu_skill_tree_button.bind("<Button-1>", open_skill_page)

    # side_menu_logout_button = ttk.Label(side_menu, text="Exit", style="Side_menu_exit_button.TLabel")
    # side_menu_logout_button.grid(row=5, column=0, pady=5)


def update_work_frame_buttons_bools():
    pass


def create_current_work_frame():
    current_work_frame = tk.Frame(start_frame)
    current_work_frame['background'] = "white"
    current_work_frame.grid(row=1, column=1, pady=30)

    current_work_title = ttk.Label(current_work_frame, text="Todo List", style="current_work_label.TLabel", justify="center")
    current_work_title.grid(row=0, column=0, columnspan=2, sticky="n", padx=10)

    reading_label = tk.Label(current_work_frame, text="Reading", foreground="#222222", background="white", font=("Times New Roman", 21))
    reading_label.grid(row=1, column=0)

    reading_completion_button = tk.Button(current_work_frame, background="#f10809", relief="flat", width=2, state="disabled")
    reading_completion_button.grid(row=1, column=1)

    writing_label = tk.Label(current_work_frame, text="Writing", foreground="#222222", background="white", font=("Times New Roman", 21))
    writing_label.grid(row=2, column=0)

    writing_completion_button = tk.Button(current_work_frame, background="green", relief="flat", width=2,
                                          state="disabled")
    writing_completion_button.grid(row=2, column=1)

    math_label = tk.Label(current_work_frame, text="Math", foreground="#222222", background="white", font=("Times New Roman", 21))
    math_label.grid(row=3, column=0)

    math_completion_button = tk.Button(current_work_frame, background="green", relief="flat", width=2,
                                          state="disabled")
    math_completion_button.grid(row=3, column=1)

    science_label = tk.Label(current_work_frame, text="Science", foreground="#222222", background="white", font=("Times New Roman", 21))
    science_label.grid(row=4, column=0)

    science_completion_button = tk.Button(current_work_frame, background="green", relief="flat", width=2,
                                          state="disabled")
    science_completion_button.grid(row=4, column=1)

    social_studies_label = tk.Label(current_work_frame, text="Social Studies", foreground="#222222", background="white", font=("Times New Roman", 21))
    social_studies_label.grid(row=5, column=0)

    social_studies_completion_button = tk.Button(current_work_frame, background="green", relief="flat", width=2,
                                          state="disabled")
    social_studies_completion_button.grid(row=5, column=1)

    arts_label = tk.Label(current_work_frame, text="Arts", foreground="#222222", background="white", font=("Times New Roman", 21))
    arts_label.grid(row=6, column=0)

    arts_completion_button = tk.Button(current_work_frame, background="grey", relief="flat", width=2,
                                          state="disabled")
    arts_completion_button.grid(row=6, column=1)

    skills_label = tk.Label(current_work_frame, text="Skills", foreground="#222222", background="white", font=("Times New Roman", 21))
    skills_label.grid(row=7, column=0)

    skills_completion_button = tk.Button(current_work_frame, background="yellow", relief="flat", width=2,
                                          state="disabled")
    skills_completion_button.grid(row=7, column=1)



# pages
home_page = tk.Frame()

skill_page = tk.Frame(root)

skills_button_frame = tk.Frame(skill_page)


speed_button = ttk.Button(home_frame, text="quick", command=start_app)
speed_button.grid(row=7)


root.mainloop()
