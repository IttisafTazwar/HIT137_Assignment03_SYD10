import cv2
import tkinter as tk
from tkinter import messagebox

# Check OpenCV version
print("OpenCV version:", cv2.__version__)

# Initialize Tkinter window
root = tk.Tk()
root.title("Tkinter Test Window")

# Display a message box to verify Tkinter is working
messagebox.showinfo("Tkinter", "Tkinter is working fine!")

# Main loop for the Tkinter window
root.mainloop()

print("OpenCV and Tkinter are working fine!")
