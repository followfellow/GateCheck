import tkinter as tk
from PIL import Image, ImageTk
import json
from Params import Params
import os
from Dicts import Layouts

global button_image
global img
global label_image
global label_img


def code_check_command():
    if code_check_var.get() == 1:
        change_to_frame4()
    else:
        change_to_frame4()


def idcard_check_command():
    if idcard_check_var.get() == 1:
        change_to_frame4()
    else:
        change_to_frame4()


def change_to_frame1():
    fm1 = Frame(window, canvas, tags='frame1')
    # fm1.image(0, 0, 'images/1.1.jpg')
    fm1.radiobutton(background_color, background_color_var)
    fm1.radiobutton(human_face, human_face_var)
    fm1.label(frame1_number)
    fm1.entry(250, 100, 40, name_var)
    fm1.entry(250, 200, 40, support_var)


def change_to_frame2():
    fm2 = Frame(window, canvas, tags='frame2')
    # fm2.image(0, 0, 'images/3.1.jpg')
    fm2.label(frame2_number)
    fm2.radiobutton(gate_form, gate_form_var)
    fm2.radiobutton(three, three_var)
    fm2.radiobutton(wing, wing_var)
    fm2.radiobutton(swing, swing_var)


def change_to_frame3():
    fm3 = Frame(window, canvas, tags='frame3')
    fm3.label(frame3_number)
    fm3.radiobutton(gate_mode, gate_mode_var)


def change_to_frame4():
    fm4 = Frame(window, canvas, tags='frame4')
    fm4.label(frame4_number)
    if code_check_var.get() == 1:
        fm4.radiobutton(code_com, code_com_var)
    fm4.checkbutton(code_check, code_check_var, command=code_check_command)
    if idcard_check_var.get() == 1:
        fm4.radiobutton(idcard_set, idcard_set_var)
    fm4.checkbutton(idcard_check, idcard_check_var, command=idcard_check_command)


def change_to_frame5():
    fm5 = Frame(window, canvas, tags='frame5')
    fm5.label(frame5_number)
    fm5.radiobutton(screen, screen_var)


class Frame:
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
        btn.place(x=557, y=5)

    def image(self, x, y, image):
        global label_image
        global label_img
        canv = tk.Canvas(self.frame, height=529, width=434)
        label_image = Image.open(image)
        label_img = ImageTk.PhotoImage(image=label_image)
        canv.create_image(x, y, anchor='nw', image=label_img)
        canv.pack(side='left')

    def checkbutton(self, mode, var, command):
        for text, x, y in mode:
            ck = tk.Checkbutton(self.frame, text=text, variable=var, bg='white', command=command)
            ck.place(x=x, y=y)

    def entry(self, x, y, width, nam):
        self.name = tk.Entry(self.frame, width=width, textvariable=nam)
        self.name.place(x=x, y=y)

    def label(self, label):
        # tk.Label(self.frame, text=self.tags).place(x=label_x, y=label_y)
        for text, color, width, x, y in label:
            tk.Label(self.frame, text=text, bg=color, width=width).place(x=x, y=y)

    def save(self):
        par.dict['BasePar']['name'] = name_var.get()
        par.dict['BasePar']['image'] = background_color_var.get()
        par.dict['BasePar']['support'] = support_var.get()
        par.dict['BasePar']['face'] = human_face_var.get()
        par.dict['GateForm']['gate_form'] = gate_form_var.get()
        par.dict['GateForm']['three'] = three_var.get()
        par.dict['GateForm']['wing'] = wing_var.get()
        par.dict['GateForm']['swing'] = swing_var.get()
        par.dict['GateMode']['gate_mode'] = gate_mode_var.get()
        par.dict['Reader']['code_check'] = code_check_var.get()
        par.dict['Reader']['code_com'] = code_com_var.get()
        par.dict['Reader']['idcard_check'] = idcard_check_var.get()
        par.dict['Reader']['idcard_set'] = idcard_set_var.get()
        par.dict['Screen']['screen'] = screen_var.get()
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
    layout = Layouts()
    # <editor-fold desc="read_layouts">
    background_color = layout.bg_color()
    human_face = layout.hm_face()
    frame1_number = layout.fm1_number()
    frame2_number = layout.fm2_number()
    frame3_number = layout.fm3_number()
    frame4_number = layout.fm4_number()
    frame5_number = layout.fm5_number()
    gate_form = layout.gt_form()
    three = layout.thr()
    wing = layout.wng()
    swing = layout.swg()
    gate_mode = layout.gt_mode()
    code_check = layout.cd_check()
    idcard_check = layout.id_check()
    code_com = layout.cd_com()
    idcard_set = layout.id_set()
    screen = layout.scr()
    # </editor-fold>
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
            "gate_mode": "单向入口",
        },
        "Reader": {
            "code_check": 1,
            "idcard_check": 1,
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
    else:
        with open('params.json', 'w') as f:  # 创建一个params.json文件
            f.write(json_str)  # 将json_str写到文件中

    par = Params('params.json')

    window = tk.Tk()
    window.title('GateCheck')

    window.geometry('800x600')
    window.resizable(False, False)
    # <editor-fold desc="read_para">
    background_color_var = tk.StringVar()
    background_color_var.set(par.dict['BasePar']['image'])
    human_face_var = tk.StringVar()
    human_face_var.set(par.dict['BasePar']['face'])
    name_var = tk.StringVar()
    name_var.set(par.dict['BasePar']['name'])
    support_var = tk.StringVar()
    support_var.set(par.dict['BasePar']['support'])
    gate_form_var = tk.StringVar()
    gate_form_var.set(par.dict['GateForm']['gate_form'])
    three_var = tk.StringVar()
    three_var.set(par.dict['GateForm']['three'])
    wing_var = tk.StringVar()
    wing_var.set(par.dict['GateForm']['wing'])
    swing_var = tk.StringVar()
    swing_var.set(par.dict['GateForm']['swing'])
    gate_mode_var = tk.StringVar()
    gate_mode_var.set(par.dict['GateMode']['gate_mode'])
    code_check_var = tk.IntVar()
    code_check_var.set(par.dict['Reader']['code_check'])
    idcard_check_var = tk.IntVar()
    idcard_check_var.set(par.dict['Reader']['idcard_check'])
    code_com_var = tk.StringVar()
    code_com_var.set(par.dict['Reader']['code_com'])
    idcard_set_var = tk.StringVar()
    idcard_set_var.set(par.dict['Reader']['idcard_set'])
    screen_var = tk.StringVar()
    screen_var.set(par.dict['Screen']['screen'])

    # </editor-fold>
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
