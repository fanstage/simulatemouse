import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

root = tk.Tk()

b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)
ttk.Label(root, text="Label", bootstyle=WARNING).pack(side=LEFT, padx=5, pady=10)
ttk.Entry(root,bootstyle="secondary").pack(side=LEFT, padx=5, pady=10)
root.mainloop()