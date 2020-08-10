import tkinter as tk
from overlay import Window
from PIL import Image, ImageTk
import tkinter as tk
from PIL import Image, ImageTk



win = Window(alpha=0.5)
img = Image.open('test.png')
# img = Image.open('test.png').convert("RGBA")
tkimage = ImageTk.PhotoImage(img)

label = tk.Label(win.root, text="Window_0", image=tkimage)
label.pack()
Window.launch()
