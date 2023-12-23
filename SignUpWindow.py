from tkinter import *
from tkinter import messagebox
import psycopg2
from UserCabinetWindow import UserCabinet

def openSighUpWindow(root, connection, driver):
    
    def isValid(string):
        char_symbols_count = sum(1 for char in string if char.isalpha())
        if char_symbols_count < 4:
            return False
        
        return True
    
    def getUserCredentials():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        phone_number = phone_number_entry.get()

        if (not isValid(username) or
            not isValid(password) or
            not isValid(email)):
            messagebox.showwarning("Warning", "Each field must contain at least 4 alphabetic symbols")
        else:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO users (username, password, email, phone_number) "
                        f"VALUES ('{username}', '{password}', '{email}', '{phone_number}');")

                    UserCabinet.openUserCabinet(False, username, root, connection, driver)
                    
            except psycopg2.errors.UniqueViolation as e:
                messagebox.showwarning("Warning", "This data has already been used")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
    
    sign_up_window = Toplevel(root)
    sign_up_window.title("Sign up")
    sign_up_window.geometry("400x400")
    sign_up_window.resizable(False, False)

    username_label = Label(sign_up_window, text="Username")
    username_label.place(x=35, y=50)
    username_entry = Entry(sign_up_window, width=30)
    username_entry.place(x=160, y=50)

    password_label = Label(sign_up_window, text="Password")
    password_label.place(x=35, y=110)
    password_entry = Entry(sign_up_window, width=30, show="*")
    password_entry.place(x=160, y=110)

    email_label = Label(sign_up_window, text="Email")
    email_label.place(x=35, y=170)
    email_entry = Entry(sign_up_window, width=30)
    email_entry.place(x=160, y=170)

    phone_number_label = Label(sign_up_window, text="Phone Number")
    phone_number_label.place(x=35, y=230)
    phone_number_entry = Entry(sign_up_window, width=30)
    phone_number_entry.place(x=160, y=230)

    sign_up_button = Button(sign_up_window, text="Sign up", command=getUserCredentials)
    sign_up_button.place(x=175, y=310)

