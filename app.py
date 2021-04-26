
import tkinter as tk
import sys
import os
# import logging

from ControlCenter import ControlCenter


if __name__ == '__main__':

    root = tk.Tk()

    ControlCenter(root).grid(sticky="nsew")
    root.grid_rowconfigure(9, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # run = ControlCenter(root)



    root.mainloop()