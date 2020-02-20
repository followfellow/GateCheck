import tkinter as tk
from PIL import Image, ImageTk
import json

global button_image
global img


def change_to_frame1():
    fm1 = Frame(window, tags='frame1')
    fm1.radiobutton(background_color, rad_var_color)
    fm1.radiobutton(human_face, rad_var_face)
    fm1.label(frame1_number)
    name=fm1.entry(300,100,40)
    support=fm1.entry(300,200,40)

def change_to_frame2():
    fm2 = Frame(window, tags='frame2')
    # fm2.label(label_x=40, label_y=40)


def change_to_frame3():
    fm3 = Frame(window, tags='frame3')
    # fm3.label(label_x=40, label_y=40)


def change_to_frame4():
    fm4 = Frame(window, tags='frame4')
    # fm4.label(label_x=40, label_y=40)


def change_to_frame5():
    fm5 = Frame(window, tags='frame5')
    # fm5.label(label_x=40, label_y=40)


class Frame:
    def __init__(self, master, tags='tags'):
        global button_image
        global img

        self.master = master
        self.tags = tags
        self.frame = tk.Frame(master)
        canvas.create_window(90, 60, width=700, height=530, anchor='nw', window=self.frame, tags=self.tags)
        button_image = Image.open('images/save.png')
        img = ImageTk.PhotoImage(image=button_image)
        btn = tk.Button(self.frame, text='保存修改', command=self.save, bg='DodgerBlue', fg='white', image=img,
                        compound='left', padx=15)
        btn.place(x=557, y=10)

    def entry(self,x,y,width):
        self.name = tk.Entry(self.frame, width=width)
        self.name.place(x=x, y=y)
        var=self.name.get()
        return var

    def label(self, label):
        # tk.Label(self.frame, text=self.tags).place(x=label_x, y=label_y)
        for text, color, width, x, y in label:
            tk.Label(self.frame, text=text, bg=color, width=width).place(x=x, y=y)

    def save(self):
        print('景区名称： ' +name.get())
        print('背景图片: ' + str(rad_var_color.get()))
        print('景区名称： ' + support.get())
        print('人脸识别: ' + str(rad_var_face.get()))

    def frame_delete(self):
        canvas.delete(self.tags)

    def radiobutton(self, mode, var):
        for text, mode, x, y in mode:
            rd = tk.Radiobutton(self.frame, text=text, variable=var,
                                value=mode)
            rd.place(x=x, y=y)


def click_button1():
    change_to_frame1()
    button1.config(fg='yellow')
    button2.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')


def click_button2():
    change_to_frame2()
    button2.config(fg='yellow')
    button1.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')


def click_button3():
    change_to_frame3()
    button3.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button4.config(fg='white')
    button5.config(fg='white')


def click_button4():
    change_to_frame4()
    button4.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button3.config(fg='white')
    button5.config(fg='white')


def click_button5():
    change_to_frame5()
    button5.config(fg='yellow')
    button1.config(fg='white')
    button2.config(fg='white')
    button3.config(fg='white')
    button4.config(fg='white')


window = tk.Tk()
window.title('GateCheck')

window.geometry('800x600')
window.resizable(False, False)

# 画布放置图片
canvas = tk.Canvas(window, height=800, width=800)
pil_image = Image.open('images/6.jpg')
image_file = ImageTk.PhotoImage(image=pil_image)
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack()

region = (1, 75, 90, 115)
region_lb = (100, 20, 250, 42)

im = Image.open('images/6.jpg')
cropped = im.crop(region)
tk_im = ImageTk.PhotoImage(cropped)
cropped_lb = im.crop(region_lb)
tk_im_lb = ImageTk.PhotoImage(cropped_lb)
lb = tk.Label(window, image=tk_im_lb, text='闸机管理系统', compound='center', borderwidth=0, padx=0, pady=0,
              fg='white', font=('黑体', 13)).place(x=100, y=20)
button1 = tk.Button(image=tk_im, command=click_button1, text='基本参数', compound='center', borderwidth=0, padx=0, pady=0,
                    fg='yellow')
button1.place(x=1, y=80)
button2 = tk.Button(image=tk_im, command=click_button2, text='闸机类型', compound='center', borderwidth=0, padx=0, pady=0,
                    fg='white')
button2.place(x=1, y=120)
button3 = tk.Button(image=tk_im, command=click_button3, text='工作模式', compound='center', borderwidth=0, padx=0, pady=0,
                    fg='white')
button3.place(x=1, y=160)
button4 = tk.Button(image=tk_im, command=click_button4, text='读卡器', compound='center', borderwidth=0, padx=0, pady=0,
                    fg='white')
button4.place(x=1, y=200)
button5 = tk.Button(image=tk_im, command=click_button5, text='显示器', compound='center', borderwidth=0, padx=0, pady=0,
                    fg='white')
button5.place(x=1, y=240)

# fm5 = Frame(window, tags='frame5')
# fm4 = Frame(window, tags='frame4')
# fm3 = Frame(window, tags='frame3')
# fm2 = Frame(window, tags='frame2')
# fm1 = Frame(window, tags='frame1')
background_color = [
    ('亮色', '亮色', 300, 150),
    ('暗色', '暗色', 400, 150),
    ('其他', '其他', 500, 150)
]
human_face = [
    ('有', '有', 300, 250),
    ('无', '无', 400, 250)
]
frame1_number = [
    ('1', 'white', '8', 50, 100),
    ('2', 'white', '8', 50, 150),
    ('3', 'white', '8', 50, 200),
    ('4', 'white', '8', 50, 250),
    ('景区名称', 'white', '10', 150, 100),
    ('背景图片', 'white', '10', 150, 150),
    ('技术支持', 'white', '10', 150, 200),
    ('人脸识别', 'white', '10', 150, 250),
    ('序号', 'SkyBlue', '8', 50, 50),
    ('项目名称', 'SkyBlue', '10', 150, 50),
    ('参数设置', 'SkyBlue', '49', 250, 50)
]
change_to_frame2()
change_to_frame3()
change_to_frame4()
change_to_frame5()

rad_var_color = tk.StringVar()
rad_var_face = tk.StringVar()
rad_var_color.set(0)
rad_var_face.set(0)
name=tk.StringVar()
support=tk.StringVar()
name.set(0)
support.set(0)
change_to_frame1()

window.mainloop()
