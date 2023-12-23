from tkinter import *
from tkinter import messagebox
from UserCabinetWindow import UserCabinet

def openLogInWindow(root, connection, driver):
    
    def getUserCredentials():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showwarning("Warning", "You must fill all fields")
        else:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT is_admin FROM users WHERE "
                    f"username = '{username}' AND password = '{password}';"
                    )
                data = cursor.fetchone()
                
                if not data:
                    messagebox.showwarning("Warning", "Such user does not exists")
                else:
                    UserCabinet.openUserCabinet(data[0], username, root, connection, driver)
    
    log_in_window = Toplevel(root)
    log_in_window.title("Log in")
    log_in_window.geometry("400x400")
    log_in_window.resizable(False, False)  

    username_label = Label(log_in_window, text="Username")
    username_label.place(x=35, y=100)

    username_entry = Entry(log_in_window, width=30)
    username_entry.place(x=160, y=100)

    password_label = Label(log_in_window, text="Password")
    password_label.place(x=35, y=200)

    password_entry = Entry(log_in_window, width=30, show="*")
    password_entry.place(x=160, y=200)

    log_in_button = Button(log_in_window, text="Log in", command=getUserCredentials)
    log_in_button.place(x=175, y=300)
