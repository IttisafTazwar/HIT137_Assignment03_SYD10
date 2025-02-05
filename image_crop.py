import cv2
import numpy as np
from tkinter import Tk, filedialog


def select_image():
    Tk().withdraw()
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    process_image(file_path)


def process_image(image_path):
    image = cv2.imread(image_path)
    clone = image.copy()
    cropping = False
    rect_start = (0, 0)
    rect_end = (0, 0)

    def save_image(cropped_image):
        """Save the cropped image."""
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            cv2.imwrite(save_path, cropped_image)
            print(f"Image saved to {save_path}")

    def mouse_callback(event, x, y, flags, param):
        nonlocal cropping, rect_start, rect_end, clone
        if event == cv2.EVENT_LBUTTONDOWN:
            cropping = True
            rect_start = (x, y)
        elif event == cv2.EVENT_MOUSEMOVE:
            if cropping:
                rect_end = (x, y)
                temp_image = clone.copy()
                mask = np.ones(temp_image.shape, dtype=np.uint8) * 255
                cv2.rectangle(mask, rect_start, rect_end, (0, 0, 0), -1)
                inverted_view = cv2.bitwise_and(temp_image, mask)
                cv2.imshow("Image", inverted_view)
        elif event == cv2.EVENT_LBUTTONUP:
            cropping = False
            rect_end = (x, y)
            mask = np.ones(image.shape, dtype=np.uint8) * 255
            cv2.rectangle(mask, rect_start, rect_end, (0, 0, 0), -1)
            cropped_image = cv2.bitwise_and(image, mask)
            cv2.imshow("Cropped Image", cropped_image)

            # After cropping, show save option
            save_image(cropped_image)

    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mouse_callback)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    select_image()
