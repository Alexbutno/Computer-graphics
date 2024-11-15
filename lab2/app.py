import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2


def load_image():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    if not filepath:
        return
    global img, original_img
    img = Image.open(filepath)
    original_img = img.copy()
    display_image(img)


def display_image(image):
    image.thumbnail((1000, 1000))
    img_tk = ImageTk.PhotoImage(image)
    label_image.config(image=img_tk)
    label_image.image = img_tk


def otsu_threshold():
    if img is None:
        messagebox.showwarning("Warning", "Load an image first!")
        return
    img_gray = img.convert("L")
    img_array = np.array(img_gray)

    _, img_binary = cv2.threshold(img_array, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_binary = Image.fromarray(np.uint8(img_binary))
    display_image(img_binary)


def laplace_filter():
    if img is None:
        messagebox.showwarning("Warning", "Load an image first!")
        return
    img_gray = img.convert("L")
    img_array = np.array(img_gray)

    laplacian = cv2.Laplacian(img_array, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    img_laplacian = Image.fromarray(laplacian)
    display_image(img_laplacian)


def gaussian_blur():
    if img is None:
        messagebox.showwarning("Warning", "Load an image first!")
        return
    img_array = np.array(img)

    blurred = cv2.GaussianBlur(img_array,(25, 25), 0)  # Размер ядра (25, 25)
    img_blurred = Image.fromarray(blurred)
    display_image(img_blurred)


def reset_image():
    if original_img is None:
        messagebox.showwarning("Warning", "Load an image first!")
        return
    display_image(original_img)


root = tk.Tk()
root.title("Image Processing Application")
root.geometry("1300x1200")

img = None
original_img = None

btn_load = tk.Button(root, text="Загрузить изображение", command=load_image)
btn_load.pack(pady=10)

btn_otsu = tk.Button(root, text="Метод Оцу", command=otsu_threshold)
btn_otsu.pack(pady=10)

btn_laplace = tk.Button(root, text="Метод Лапласа", command=laplace_filter)
btn_laplace.pack(pady=10)

btn_gaussian = tk.Button(root, text="Сглаживающий фильтр (Гауссовский)",
                         command=gaussian_blur)
btn_gaussian.pack(pady=10)

btn_reset = tk.Button(root, text="Сбросить изображение", command=reset_image)
btn_reset.pack(pady=10)

label_image = tk.Label(root)
label_image.pack(pady=10)

root.mainloop()