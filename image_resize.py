import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def select_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if not file_path:
        print("No file selected!")
        return

    global original_img, resized_img, img_label

    original_img = cv2.imread(file_path)
    if original_img is None:
        print("Error: Image not loaded. Check file path!")
        return

    # Convert image to RGB (OpenCV loads images in BGR format)
    original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    resized_img = original_img.copy()

    display_image(resized_img)


def resize_image(value):
    global resized_img
    scale = int(value) / 100  # Convert slider value (1-100) to scale factor
    new_size = (int(original_img.shape[1] * scale), int(original_img.shape[0] * scale))

    # Resize but maintain original for export
    resized_img = cv2.resize(original_img, new_size, interpolation=cv2.INTER_LINEAR)
    display_image(resized_img)


def display_image(img):
    global img_label
    img = Image.fromarray(img)  # Convert OpenCV image to PIL format
    img = ImageTk.PhotoImage(img)

    img_label.config(image=img)
    img_label.image = img  # Keep a reference to prevent garbage collection


def save_image():
    if resized_img is None:
        print("No image to save!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if file_path:
        cv2.imwrite(file_path, cv2.cvtColor(resized_img, cv2.COLOR_RGB2BGR))
        print(f"Image saved at {file_path}")


# GUI Setup
root = tk.Tk()
root.title("Image Resizer")

btn_select = tk.Button(root, text="Select Image", command=select_image)
btn_select.pack()

img_label = tk.Label(root)
img_label.pack()

slider = tk.Scale(root, from_=10, to=100, orient="horizontal", label="Resize", command=resize_image)
slider.pack()

btn_save = tk.Button(root, text="Save Image", command=save_image)
btn_save.pack()

root.mainloop()
