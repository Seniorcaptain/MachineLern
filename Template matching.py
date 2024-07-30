import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

class HospitalInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("HOSPITAL INTERFACE")
        self.geometry("640x400")
        self.iconbitmap('icon.ico')

        self.label_frame = ttk.LabelFrame(self, text="Open a File")
        self.label_frame.grid(column=0, row=1, padx=20, pady=20)

        self.create_button()

        self.img_label = tk.Label(self)
        self.img_label.grid(column=0, row=0)

    def create_button(self):
        button = ttk.Button(self.label_frame, text="Open Image", command=self.show_img)
        button.grid(column=0, row=0)

    def show_img(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            self.img_label.config(image=photo)
            self.img_label.image = photo  # Keep a reference to avoid garbage collection

if __name__ == '__main__':
    app = HospitalInterface()
    app.mainloop()
