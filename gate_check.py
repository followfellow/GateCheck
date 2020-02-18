import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



def click_button1():
    print(1)


def click_button2():
    print(2)


window = tk.Tk()
window.title('GateCheck')

tabControl = ttk.Notebook(window)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='Tab 1')      # Add the tab
tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible


window.geometry('800x600')
# 画布放置图片
canvas = tk.Canvas(tab1, height=800, width=800)
pil_image = Image.open('images/1.jpg')
image_file = ImageTk.PhotoImage(image=pil_image)
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
canvas.pack(side='top')

button1 = tk.Button(tab1, text="button1", command=click_button1, width=10, height=1)
button1.place(x=10,y=100,anchor='nw')

button2 = tk.Button(tab2, text="button2", command=click_button2, width=10, height=1)
button2.place(x=10,y=100,anchor='nw')

# # 标签 用户名密码
# tk.Label(window, text='用户名:').place(x=100, y=150)
# tk.Label(window, text='密码:').place(x=100, y=190)
# # 用户名输入框
# var_usr_name = tk.StringVar()
# entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
# entry_usr_name.place(x=160, y=150)
# # 密码输入框
# var_usr_pwd = tk.StringVar()
# entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
# entry_usr_pwd.place(x=160, y=190)

window.mainloop()
