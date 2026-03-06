import tkinter as tk
from database.db import create_table
from ui.student_ui import StudentUI

create_table()

root = tk.Tk()
app = StudentUI(root)
root.mainloop()