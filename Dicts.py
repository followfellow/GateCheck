class Layouts:
    def __init__(self):
        self.background_color = [
            ('亮色', '亮色', 250, 150),
            ('暗色', '暗色', 350, 150),
            ('其他', '其他', 450, 150)
        ]
        self.human_face = [
            ('有', '有', 250, 250),
            ('无', '无', 350, 250)
        ]
        self.frame1_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('4', 'white', '8', 50, 250),
            ('5', 'white', '8', 50, 300),
            ('6', 'white', '8', 50, 350),
            ('景区名称', 'white', '10', 150, 100),
            ('背景图片', 'white', '10', 150, 150),
            ('技术支持', 'white', '10', 150, 200),
            ('人脸识别', 'white', '10', 150, 250),
            ('后台地址', 'white', '10', 150, 300),
            ('闸机编号', 'white', '10', 150, 350),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('项目名称', 'SkyBlue', '10', 150, 50),
            ('参数设置', 'SkyBlue', '44', 250, 50)
        ]
        self.frame2_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('三辊闸机', 'white', '10', 150, 100),
            ('翼门闸机', 'white', '10', 150, 150),
            ('摆门闸机', 'white', '10', 150, 200),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('闸机型式', 'SkyBlue', '10', 150, 50),
            ('闸机控制器串口号', 'SkyBlue', '44', 250, 50),
            ('选择', 'SkyBlue', '8', 580, 50)
        ]
        self.frame3_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('4', 'white', '8', 50, 250),
            ('5', 'white', '8', 50, 300),
            ('单向入口', 'white', '8', 150, 100),
            ('单向出口', 'white', '8', 150, 150),
            ('单向出口', 'white', '8', 150, 200),
            ('双向进出', 'white', '8', 150, 250),
            ('双向进出', 'white', '8', 150, 300),
            ('单向进入', 'white', '8', 250, 100),
            ('出口计数', 'white', '8', 250, 150),
            ('出口不计数', 'white', '10', 250, 200),
            ('正向刷卡，出口计数', 'white', '17', 250, 250),
            ('正向刷卡，出口不计数', 'white', '19', 250, 300),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('工作模式', 'SkyBlue', '10', 150, 50),
            ('内容', 'SkyBlue', '44', 250, 50),
            ('选择', 'SkyBlue', '8', 580, 50)
        ]
        self.frame4_number = [
            ('1', 'white', '8', 50, 150),
            ('1', 'white', '8', 50, 300),
            ('2', 'white', '8', 50, 350),
            ('3', 'white', '8', 50, 400),
            ('4', 'white', '8', 50, 450),
            ('主二维码', 'white', '10', 150, 150),
            ('新中新DJ1', 'white', '10', 150, 300),
            ('新中新DJ2', 'white', '10', 150, 350),
            ('中控1', 'white', '7', 150, 400),
            ('中控2', 'white', '7', 150, 450),
            ('身份证+RFID卡二合一', 'white', '18', 250, 300),
            ('身份证', 'white', '6', 250, 350),
            ('身份证', 'white', '6', 250, 400),
            ('身份证', 'white', '6', 250, 450),
            ('二维码门票阅读器配置', 'white', '20', 50, 70),
            ('序号', 'SkyBlue', '8', 50, 100),
            ('读卡器', 'SkyBlue', '10', 150, 100),
            ('读卡器串口号', 'SkyBlue', '44', 250, 100),
            ('身份证阅读器配置', 'white', '16', 50, 220),
            ('序号', 'SkyBlue', '8', 50, 250),
            ('阅读器型号', 'SkyBlue', '10', 150, 250),
            ('说明', 'SkyBlue', '44', 250, 250),
            ('选择', 'SkyBlue', '8', 580, 250)
        ]
        self.frame5_number = [
            ('1', 'white', '8', 50, 100),
            ('2', 'white', '8', 50, 150),
            ('3', 'white', '8', 50, 200),
            ('4', 'white', '8', 50, 250),
            ('5', 'white', '8', 50, 300),
            ('6', 'white', '8', 50, 350),
            ('7', 'white', '8', 50, 400),
            ('6.5寸', 'white', '10', 150, 100),
            ('6.5寸', 'white', '10', 150, 150),
            ('8.4寸', 'white', '10', 150, 200),
            ('8.4寸', 'white', '10', 150, 250),
            ('10.2寸', 'white', '10', 150, 300),
            ('10.2寸', 'white', '10', 150, 350),
            ('12.5寸', 'white', '10', 150, 400),
            ('800*600', 'white', '7', 300, 100),
            ('600*800', 'white', '7', 300, 150),
            ('1024*768', 'white', '8', 300, 200),
            ('768*1024', 'white', '8', 300, 250),
            ('1024*768', 'white', '8', 300, 300),
            ('768*1024', 'white', '8', 300, 350),
            ('900*1600', 'white', '8', 300, 400),
            ('横放', 'white', '4', 480, 100),
            ('竖放', 'white', '4', 480, 150),
            ('横放', 'white', '4', 480, 200),
            ('竖放', 'white', '4', 480, 250),
            ('横放', 'white', '4', 480, 300),
            ('竖放', 'white', '4', 480, 350),
            ('竖放', 'white', '4', 480, 400),
            ('序号', 'SkyBlue', '8', 50, 50),
            ('屏幕大小', 'SkyBlue', '10', 150, 50),
            ('分辨率', 'SkyBlue', '25', 250, 50),
            ('放置形式', 'SkyBlue', '18', 440, 50),
            ('选择', 'SkyBlue', '8', 580, 50)
        ]
        self.gate_form = [
            ('', '三辊闸机', 600, 100),
            ('', '翼闸', 600, 150),
            ('', '摆闸', 600, 200)
        ]
        self.three = [
            ('COM1', 'COM1', 250, 100),
            ('COM2', 'COM2', 330, 100),
            ('COM3', 'COM3', 410, 100),
            ('COM4', 'COM4', 490, 100)
        ]
        self.wing = [
            ('COM1', 'COM1', 250, 150),
            ('COM2', 'COM2', 330, 150),
            ('COM3', 'COM3', 410, 150),
            ('COM4', 'COM4', 490, 150)
        ]
        self.swing = [
            ('COM1', 'COM1', 250, 200),
            ('COM2', 'COM2', 330, 200),
            ('COM3', 'COM3', 410, 200),
            ('COM4', 'COM4', 490, 200)
        ]
        self.gate_mode = [
            ('', '单向入口', 600, 100),
            ('', '单出计数', 600, 150),
            ('', '单出不计', 600, 200),
            ('', '双向出计', 600, 250),
            ('', '双向不计', 600, 300)
        ]
        self.code_check = [
            ('二维码', 100, 15)
        ]
        self.idcard_check = [
            ('身份证', 200, 15)
        ]
        self.code_com = [
            ('COM1', 'COM1', 250, 150),
            ('COM2', 'COM2', 330, 150),
            ('COM3', 'COM3', 410, 150),
            ('COM4', 'COM4', 490, 150)
        ]
        self.idcard_set = [
            ('', 'synjo+RFID', 600, 300),
            ('', 'synjo', 600, 350),
            ('', 'zk1', 600, 400),
            ('', 'zk2', 600, 450)
        ]
        self.screen = [
            ('', '6.5_800*600', 600, 100),
            ('', '6.5_600*800', 600, 150),
            ('', '8.4_1024*768', 600, 200),
            ('', '8.4_768*1024', 600, 250),
            ('', '10.2_1024*768', 600, 300),
            ('', '10.2_768*1024', 600, 350),
            ('', '12.5_900*1600', 600, 400)
        ]

    def bg_color(self):
        return self.background_color

    def hm_face(self):
        return self.human_face

    def fm1_number(self):
        return self.frame1_number

    def fm2_number(self):
        return self.frame2_number

    def fm3_number(self):
        return self.frame3_number

    def fm4_number(self):
        return self.frame4_number

    def fm5_number(self):
        return self.frame5_number

    def gt_form(self):
        return self.gate_form

    def thr(self):
        return self.three

    def wng(self):
        return self.wing

    def swg(self):
        return self.swing

    def gt_mode(self):
        return self.gate_mode

    def cd_check(self):
        return self.code_check

    def id_check(self):
        return self.idcard_check

    def cd_com(self):
        return self.code_com

    def id_set(self):
        return self.idcard_set

    def scr(self):
        return self.screen
