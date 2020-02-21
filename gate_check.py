import tkinter as tk
from PIL import Image, ImageTk
import json
from Params import params
import os
from Dicts import layouts

global button_image
global img


def change_to_frame1():
    fm1 = frame(window, canvas, tags='frame1')
    fm1.radiobutton(background_color, rad_var_color)
    fm1.radiobutton(human_face, rad_var_face)
    fm1.label(frame1_number)
    fm1.entry(300, 100, 40, name)
    fm1.entry(300, 200, 40, support)


def change_to_frame2():
    fm2 = frame(window, canvas, tags='frame2')
    fm2.radiobutton(gate_form, gate_form_var)
    fm2.radiobutton(three, three_var)
    fm2.radiobutton(wing, wing_var)
    fm2.radiobutton(swing, swing_var)



def change_to_frame3():
    fm3 = frame(window, canvas, tags='frame3')


def change_to_frame4():
    fm4 = frame(window, canvas, tags='frame4')


def change_to_frame5():
    fm5 = frame(window, canvas, tags='frame5')


class frame:
    def __init__(self, master, canvas, tags='tags'):
        global button_image
        global img

        self.master = master
        self.tags = tags
        self.frame = tk.Frame(master, bg='white')
        canvas.create_window(90, 60, width=700, height=530, anchor='nw', window=self.frame, tags=self.tags)
        button_image = Image.open('images/save.png')
        img = ImageTk.PhotoImage(image=button_image)
        btn = tk.Button(self.frame, text='保存修改', command=self.save, bg='DodgerBlue', fg='white', image=img,
                        compound='left', padx=15)
        btn.place(x=557, y=10)

    def entry(self, x, y, width, nam):
        self.name = tk.Entry(self.frame, width=width, textvariable=nam)
        self.name.place(x=x, y=y)

    def label(self, label):
        # tk.Label(self.frame, text=self.tags).place(x=label_x, y=label_y)
        for text, color, width, x, y in label:
            tk.Label(self.frame, text=text, bg=color, width=width).place(x=x, y=y)

    def save(self):
        par.dict['BasePar']['name'] = name.get()
        par.dict['BasePar']['image'] = rad_var_color.get()
        par.dict['BasePar']['support'] = support.get()
        par.dict['BasePar']['face'] = rad_var_face.get()
        par.dict['GateForm']['gate_form'] = gate_form_var.get()
        par.dict['GateForm']['three'] = three_var.get()
        par.dict['GateForm']['wing'] = wing_var.get()
        par.dict['GateForm']['swing'] = swing_var.get()
        par.save('params.json')

    def radiobutton(self, mode, var):
        for text, mode, x, y in mode:
            rd = tk.Radiobutton(self.frame, text=text, variable=var,
                                value=mode, bg='white')
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


if __name__ == '__main__':
    layout = layouts()
    background_color = layout.bg_color()
    human_face = layout.hm_face()
    frame1_number = layout.fm1_number()
    gate_form = layout.gt_form()
    three = layout.thr()
    wing = layout.wng()
    swing = layout.swg()

    parameters = {
        "BasePar": {
            "name": "",
            "image": "亮色",
            "support": "上海大漠电子科技股份有限公司",
            "face": "无",
        },
        "GateForm": {
            "gate_form": "三辊闸机",
            "three": "COM2",
            "wing": "COM2",
            "swing": "COM2",
        },
        "GateMode": {
            "gate_mode": "单向进入",
        },
        "Reader": {
            "code_check": "checked",
            "idcard_check": "checked",
            "code_com": "COM3",
            "idcard_set": "synjo+RFID",
        },
        "Screen": {
            "screen": "6.5_800*600",
        }
    }
    json_str = json.dumps(parameters, indent=4)

    if os.path.isfile('params.json'):
        with open('params.json', 'r') as f:
            a = json.load(f)
            print(a)
    else:
        with open('params.json', 'w') as f:  # 创建一个params.json文件
            f.write(json_str)  # 将json_str写到文件中

    par = params('params.json')

    window = tk.Tk()
    window.title('GateCheck')

    window.geometry('800x600')
    window.resizable(False, False)

    rad_var_color = tk.StringVar()
    rad_var_color.set(par.dict['BasePar']['image'])
    rad_var_face = tk.StringVar()
    rad_var_face.set(par.dict['BasePar']['face'])
    name = tk.StringVar()
    name.set(par.dict['BasePar']['name'])
    support = tk.StringVar()
    support.set(par.dict['BasePar']['support'])
    gate_form_var = tk.StringVar()
    gate_form_var.set(par.dict['GateForm']['gate_form'])
    three_var = tk.StringVar()
    three_var.set(par.dict['GateForm']['three'])
    wing_var = tk.StringVar()
    wing_var.set(par.dict['GateForm']['wing'])
    swing_var = tk.StringVar()
    swing_var.set(par.dict['GateForm']['swing'])

    # 画布放置图片
    canvas = tk.Canvas(window, height=800, width=800)
    pil_image = Image.open('images/6.jpg')
    image_file = ImageTk.PhotoImage(image=pil_image)
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack()
    # <editor-fold desc="button">
    region = (1, 75, 90, 115)
    region_lb = (100, 20, 250, 42)

    im = Image.open('images/6.jpg')
    cropped = im.crop(region)
    tk_im = ImageTk.PhotoImage(cropped)
    cropped_lb = im.crop(region_lb)
    tk_im_lb = ImageTk.PhotoImage(cropped_lb)
    lb = tk.Label(window, image=tk_im_lb, text='闸机管理系统', compound='center', borderwidth=0, padx=0, pady=0,
                  fg='white', font=('黑体', 13)).place(x=100, y=20)
    button1 = tk.Button(image=tk_im, command=click_button1, text='基本参数', compound='center', borderwidth=0, padx=0,
                        pady=0,
                        fg='yellow')
    button1.place(x=1, y=80)
    button2 = tk.Button(image=tk_im, command=click_button2, text='闸机类型', compound='center', borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button2.place(x=1, y=120)
    button3 = tk.Button(image=tk_im, command=click_button3, text='工作模式', compound='center', borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button3.place(x=1, y=160)
    button4 = tk.Button(image=tk_im, command=click_button4, text='读卡器', compound='center', borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button4.place(x=1, y=200)
    button5 = tk.Button(image=tk_im, command=click_button5, text='显示器', compound='center', borderwidth=0, padx=0,
                        pady=0,
                        fg='white')
    button5.place(x=1, y=240)
    # </editor-fold>
    change_to_frame2()
    change_to_frame3()
    change_to_frame4()
    change_to_frame5()
    change_to_frame1()

    window.mainloop()
