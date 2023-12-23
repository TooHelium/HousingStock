import psycopg2
from neo4j import GraphDatabase
from tkinter import *
from tkinter import messagebox

import SignUpWindow
import LogInWindow

try:
    connection = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "parol1234",
        database = "HousingStock",
        )
    connection.autocommit = True
except Exception as ex:
    messagebox.showerror("Error", f"Error connection to PostgreSQL db: {ex}")

try:
    uri_graph = "bolt://localhost:7687"
    username_graph = "neo4j"
    password_graph = "parolforneo4j"
    driver = GraphDatabase.driver(uri_graph,
                                  auth=(username_graph, password_graph))
except Exception as ex:
    messagebox.showerror("Error", f"Error connection to Neo4j db: {ex}")

root = Tk()
root.title("Authorization")
root.geometry("300x300")
root.resizable(False, False)

button_log_in = Button(root, text="Log in", command=lambda: LogInWindow.openLogInWindow(root, connection, driver))
button_log_in.place(x=50, y=200)

button_sigh_up = Button(root, text="Sign up", command=lambda: SignUpWindow.openSighUpWindow(root, connection, driver))
button_sigh_up.place(x=200, y=200)

label = Label(root, text="Welcome to the App", font=("Helvetica", 16))
label.place(x=40, y=100)

root.mainloop()

connection.close()
print("[INFO] PostgreSQL connection closed")

driver.close()
print("Neo4j connection closed")
