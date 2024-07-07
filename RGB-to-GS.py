from PIL import Image
import tkinter as tk
from tkinter import filedialog

def open_image():
    # باز کردن دیالوگ فایل برای انتخاب فایل تصویر
    file_path = filedialog.askopenfilename()
    if file_path:
        convert_to_grayscale(file_path)

def convert_to_grayscale(file_path):
    # باز کردن فایل تصویر
    img = Image.open(file_path)
    # تبدیل تصویر به خاکستری
    grayscale_img = img.convert("L")
    # ذخیره تصویر خاکستری
    grayscale_img.save("grayscale_image.png")
    print("Converted Successfully, Check Your Desktop.")

def main():
    root = tk.Tk()
    root.title("تبدیل تصویر RGB به خاکستری")
    root.geometry("300x100")

    # ایجاد یک دکمه برای باز کردن دیالوگ فایل
    open_button = tk.Button(root, text="باز کردن تصویر", command=open_image)
    open_button.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()


#ByAraw