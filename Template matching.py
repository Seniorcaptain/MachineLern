from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")

class Root():
    def __init__(self):
        super(Root, self).__init__()
        self.title("HOSPITAL INTERFACE")
        self.minimise(640, 400)
        self.wm_iconbitmap('icon.ico')

        self.labelFrame = ttk.labelFrame(self, text="Open a File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.button()


        def showimg(self):
            result = filedialog.askopenfile()
            load = Image.open(result)
            render = ImageTk.photoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=0, y=0)



if __name__ == '__main__':

