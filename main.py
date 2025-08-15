import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def open_file():
    global image_selected, img
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp")]
    )
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((500, 500))
        tk_img = ImageTk.PhotoImage(img)
        image_label.config(image=tk_img)
        image_label.image = tk_img
        image_selected = True


def convert():
    global img

    if not image_selected:
        messagebox.showerror("Error", "No Image Selected")
        return

    try:
        file_name = filedialog.asksaveasfilename(
            defaultextension=f".{selected_format.get().lower()}",
            filetypes=[(f"{selected_format.get()} files", f"*.{selected_format.get().lower()}")]
        )
        if file_name:
            save_format = selected_format.get()
            save_image = img

            if save_format.upper() == "JPG":
                save_image = img.convert("RGB")
                save_format = "JPEG"

            save_image.save(file_name, save_format)
            messagebox.showinfo("Success", f"Image saved as {file_name}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert image:\n{e}")


root = tk.Tk()
root.title('Image Converter')
root.geometry('500x500')

image_selected = False

label = tk.Label(root, text="Image Converter", font=("Arial", 16))
label.pack(pady=20)
button = tk.Button(root, text="Select Image", font=("Arial", 14), command=open_file)
button.pack(pady=10)
formats = ["PNG", "JPG", "WEBP"]
selected_format = tk.StringVar(value=formats[0])
format_menu = tk.OptionMenu(root, selected_format, *formats)
format_menu.pack(pady=10)
button = tk.Button(root, text="Convert", font=("Arial", 14), command=convert)
button.pack(pady=10)
image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()