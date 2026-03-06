import tkinter as tk
from tkinter import ttk
from services.student_service import *
from models.student_model import Student


class StudentUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("900x500")

        self.create_form()
        self.create_table()
        self.load_students()

    def create_form(self):

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame,text="Name").grid(row=0,column=0)
        self.name = tk.Entry(frame)
        self.name.grid(row=0,column=1)

        tk.Label(frame,text="Age").grid(row=1,column=0)
        self.age = tk.Entry(frame)
        self.age.grid(row=1,column=1)

        tk.Label(frame,text="Department").grid(row=2,column=0)
        self.dept = tk.Entry(frame)
        self.dept.grid(row=2,column=1)

        tk.Label(frame,text="Email").grid(row=3,column=0)
        self.email = tk.Entry(frame)
        self.email.grid(row=3,column=1)

        tk.Button(frame,text="Add Student",command=self.add_student).grid(row=4,column=0)
        tk.Button(frame,text="Delete Student",command=self.delete_student).grid(row=4,column=1)
        tk.Button(frame,text="Update Student",command=self.update_student).grid(row=4,column=2)

        tk.Label(frame,text="Search").grid(row=5,column=0)

        self.search = tk.Entry(frame)
        self.search.grid(row=5,column=1)

        tk.Button(frame,text="Search",command=self.search_student_ui).grid(row=5,column=2)

        tk.Button(frame,text="List Students",command=self.load_students).grid(row=6,column=1)

    def create_table(self):

        columns = ("ID","Name","Age","Dept","Email")

        self.tree = ttk.Treeview(self.root,columns=columns,show="headings")

        for col in columns:
            self.tree.heading(col,text=col)
            self.tree.column(col,width=150)

        self.tree.pack(fill="both",expand=True)

        self.tree.bind("<ButtonRelease-1>", self.select_student)

    def load_students(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        students = get_students()

        for student in students:
            self.tree.insert("", "end", values=student)

    def add_student(self):

        student = Student(
            self.name.get(),
            self.age.get(),
            self.dept.get(),
            self.email.get()
        )

        add_student(student)

        self.load_students()

    def delete_student(self):

        selected = self.tree.selection()

        if selected:

            student_id = self.tree.item(selected[0])["values"][0]

            delete_student(student_id)

            self.load_students()

    def update_student(self):

        selected = self.tree.selection()

        if selected:

            student_id = self.tree.item(selected[0])["values"][0]

            update_student(
                student_id,
                self.name.get(),
                self.age.get(),
                self.dept.get(),
                self.email.get()
            )

            self.load_students()

    def search_student_ui(self):

        keyword = self.search.get()

        rows = search_student(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in rows:
            self.tree.insert("", "end", values=row)

    def select_student(self,event):

        selected = self.tree.focus()

        values = self.tree.item(selected,"values")

        if values:

            self.name.delete(0,tk.END)
            self.name.insert(0,values[1])

            self.age.delete(0,tk.END)
            self.age.insert(0,values[2])

            self.dept.delete(0,tk.END)
            self.dept.insert(0,values[3])

            self.email.delete(0,tk.END)
            self.email.insert(0,values[4])