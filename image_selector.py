import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Function to open file dialog and select an image
def select_image():
    # Open the file dialog to choose an image
    file_path = filedialog.askopenfilename()

    if file_path:
        # Read the image using OpenCV
        image = cv2.imread(file_path)

        # Convert the image from BGR (OpenCV format) to RGB (Pillow format)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Create a PIL Image object
        pil_image = Image.fromarray(image_rgb)

        # Resize the image to create a thumbnail
        thumbnail = pil_image.resize((150, 150))

        # Convert the thumbnail to ImageTk format for displaying in Tkinter
        thumbnail_tk = ImageTk.PhotoImage(thumbnail)

        # Update the label with the new thumbnail image
        label.config(image=thumbnail_tk)
        label.image = thumbnail_tk  # Keep a reference to avoid garbage collection

        # Save the thumbnail image
        save_image(thumbnail)


# Function to save the thumbnail image
def save_image(image):
    # Open the file dialog to choose where to save the image
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    if save_path:
        # Save the image as a PNG file
        image.save(save_path)


# Create the main window
root = tk.Tk()
root.title("Image Thumbnail Viewer")

# Create a button to select an image
button = tk.Button(root, text="Select Image", command=select_image)
button.pack()

# Create a label to display the image thumbnail
label = tk.Label(root)
label.pack()

# Run the Tkinter event loop
root.mainloop()
