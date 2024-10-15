import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

conn = None
cursor = None

# Connecting Database
def create_database():
    global conn, cursor
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",  # or your MySQL server IP
            user="root",  # Replace with your MySQL username
            password="Akshat@2004",  # Replace with your MySQL password
            database="student_registration_db"  # Replace with your database name
        )
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                contact VARCHAR(50),
                email VARCHAR(255),
                roll_no INT,
                branch VARCHAR(50),
                teacher_id INT,
                course_id INT
            )
        ''')
        conn.commit()
    except Error as e:
        messagebox.showerror("Error", f"Database connection failed: {e}")
        conn = None
        cursor = None

def check_db_connection():
    if conn is None or cursor is None:
        messagebox.showerror("Error", "Database connection not established. Please try again.")
        return False
    return True

# To Register a new student
def register():
    if not check_db_connection():
        return

    name = name_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    roll_no = roll_no_entry.get()
    branch = branch_entry.get()
    teacher_id = teacher_id_entry.get()
    course_id = course_id_entry.get()

    if not name or not contact or not email or not roll_no or not branch or not teacher_id or not course_id:
        messagebox.showinfo("Error", "Please fill in all fields.")
        return

    try:
        cursor.execute('''
            INSERT INTO STUD_REGISTRATION (name, contact, email, roll_no, branch, teacher_id, course_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (name, contact, email, int(roll_no), branch, int(teacher_id), int(course_id)))
        conn.commit()
        messagebox.showinfo("Success", "Student registered successfully.")
        clear_fields()
    except Error as e:
        messagebox.showerror("Error", f"Failed to register student: {e}")

# Displays all students
def display_data():
    if not check_db_connection():
        return

    try:
        cursor.execute("SELECT * FROM STUD_REGISTRATION")
        data = cursor.fetchall()

        tree.delete(*tree.get_children())
        for row in data:
            tree.insert("", "end", values=row)
    except Error as e:
        messagebox.showerror("Error", f"Failed to display data: {e}")

# Delete a student from the database
def delete_data():
    if not check_db_connection():
        return

    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo("Error", "Please select a student to delete.")
        return

    item_id = tree.item(selected_item)['values'][0]
    if messagebox.askyesno("Confirm", "Are you sure you want to delete this record?"):
        try:
            cursor.execute("DELETE FROM STUD_REGISTRATION WHERE id = %s", (item_id,))
            conn.commit()
            messagebox.showinfo("Success", "Student deleted successfully.")
            display_data()
        except Error as e:
            messagebox.showerror("Error", f"Failed to delete student: {e}")

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    roll_no_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    teacher_id_entry.delete(0, tk.END)
    course_id_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Student Registration System")

window.state('zoomed')

window.configure(bg="#f0f0f0")  # Light grayish background

heading_label = tk.Label(window, text="Student Management System", font=("Arial", 30, "bold"), fg="darkblue",
                         bg="#f0f0f0")
heading_label.grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")
heading_label.grid_columnconfigure(0, weight=1)  # Make sure it stretches across all columns

label_font = ("Arial", 12)
entry_width = 40

name_label = tk.Label(window, text="Name:", font=label_font, bg="#f0f0f0")
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(window, width=entry_width)
name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

contact_label = tk.Label(window, text="Contact:", font=label_font, bg="#f0f0f0")
contact_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
contact_entry = tk.Entry(window, width=entry_width)
contact_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

email_label = tk.Label(window, text="Email:", font=label_font, bg="#f0f0f0")
email_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
email_entry = tk.Entry(window, width=entry_width)
email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

roll_no_label = tk.Label(window, text="Roll No:", font=label_font, bg="#f0f0f0")
roll_no_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
roll_no_entry = tk.Entry(window, width=entry_width)
roll_no_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

branch_label = tk.Label(window, text="Branch:", font=label_font, bg="#f0f0f0")
branch_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
branch_entry = tk.Entry(window, width=entry_width)
branch_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

teacher_id_label = tk.Label(window, text="Teacher ID:", font=label_font, bg="#f0f0f0")
teacher_id_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
teacher_id_entry = tk.Entry(window, width=entry_width)
teacher_id_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

course_id_label = tk.Label(window, text="Course ID:", font=label_font, bg="#f0f0f0")
course_id_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
course_id_entry = tk.Entry(window, width=entry_width)
course_id_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

# Buttons
button_font = ("Arial", 12, "bold")

register_button = tk.Button(window, text="Register", command=register, bg="green", fg="white", font=button_font)
register_button.grid(row=8, column=0, padx=10, pady=10)

display_button = tk.Button(window, text="Display Data", command=display_data, bg="blue", fg="white", font=button_font)
display_button.grid(row=8, column=1, padx=10, pady=10)

delete_button = tk.Button(window, text="Delete", command=delete_data, bg="red", fg="white", font=button_font)
delete_button.grid(row=8, column=2, padx=10, pady=10)

clear_button = tk.Button(window, text="Clear", command=clear_fields, bg="orange", fg="white", font=button_font)
clear_button.grid(row=8, column=3, padx=10, pady=10)

tree = ttk.Treeview(window, columns=("ID", "Name", "Contact", "Email", "Roll No", "Branch", "Teacher ID", "Course ID"),
                    show='headings')
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Contact", text="Contact")
tree.heading("Email", text="Email")
tree.heading("Roll No", text="Roll No")
tree.heading("Branch", text="Branch")
tree.heading("Teacher ID", text="Teacher ID")
tree.heading("Course ID", text="Course ID")

for col in tree["columns"]:
    tree.column(col, anchor="center")
    tree.heading(col, text=col)

tree.grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

window.grid_rowconfigure(9, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

create_database()
display_data()
window.mainloop()

# Close the database connection on exit
if conn:
    cursor.close()
    conn.close()
