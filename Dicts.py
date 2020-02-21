class layouts:
    def __init__(self):
        self.background_color = [
            ('亮色', '亮色', 300, 150),
            ('暗色', '暗色', 400, 150),
            ('其他', '其他', 500, 150)
        ]
        self.human_face = [
            ('有', '有', 300, 250),
            ('无', '无', 400, 250)
        ]
        self.frame1_number = [
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
            ('', '单向入口', 300, 150),
            ('', '单出计数', 400, 150),
            ('', '单出不计', 500, 150),
            ('', '双向出计', 500, 150),
            ('', '双向不计', 500, 150)
        ]
        self.code_com = [
            ('COM1', 'COM1', 300, 150),
            ('COM2', 'COM2', 400, 150),
            ('COM3', 'COM3', 500, 150),
            ('COM4', 'COM4', 500, 150)
        ]
        self.idcard_set = [
            ('', 'synjo+RFID', 300, 150),
            ('', 'synjo', 400, 150),
            ('', 'zk1', 500, 150),
            ('', 'zk2', 500, 150)
        ]
        self.screen = [
            ('', '6.5横', 300, 150),
            ('', '6.5竖', 400, 150),
            ('', '8.4横', 500, 150),
            ('', '8.4竖', 500, 150),
            ('', '10.2横', 500, 150),
            ('', '10.2竖', 500, 150),
            ('', '12.5竖', 500, 150)
        ]

    def bg_color(self):
        return self.background_color

    def hm_face(self):
        return self.human_face

    def fm1_number(self):
        return self.frame1_number

    def gt_form(self):
        return self.gate_form

    def thr(self):
        return self.three

    def wng(self):
        return self.wing

    def swg(self):
        return self.swing
