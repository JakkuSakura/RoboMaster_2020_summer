import os  # line:1
import sys  # line:2
import time  # line:3
import random  # line:4
import _thread  # line:5
import tkinter as tk  # line:6
import tkinter.font as tf  # line:7
import tkinter.scrolledtext  # line:8

from PIL.ImageTk import PhotoImage
from link_search import link_search  # line:9

sys.path.append("../read_picture/")  # line:10
import read_picture  # line:11


class auto_grader:  # line:14
    def __init__(self, enable_ui=True):  # line:15
        if enable_ui:  # line:16
            _thread.start_new_thread(self.ui, tuple())  # line:17
            time.sleep(1)  # line:18
        img_path = '../mnist_data/t10k-images.idx3-ubyte'  # line:19
        lbl_path = '../mnist_data/t10k-labels.idx1-ubyte'  # line:20
        img = self.random_image(img_path, lbl_path)  # line:21
        self.load_images()  # line:22
        self.ls = link_search(img)  # line:23
        self.scores = [50, 20, 10, 0, -10, -100, -100]  # line:24
        self.doublescores = [100, 20, 10, 0]  # line:25
        self.current_score = 0  # line:27
        self.round = 0  # line:28
        self.enable_ui = enable_ui  # line:29

    def random_image(self, image_path, label_path):  # line:31
        image_list, label_list = read_picture.read_image_data(image_path, label_path)  # line:33
        sample = random.sample(range(0, len(image_list)), 32)  # line:34
        print('随机取样完成')  # line:35
        color_dict = dict()  # line:36
        for real_img_index in sample:  # line:37
            color_dict[real_img_index] = random.randint(0, 2)  # line:38
        for img_index in range(len(sample)):  # line:39
            image_label = label_list[sample[img_index]]  # line:40
            for i in range(random.randint(0, len(image_list) // 2),
                           len(image_list)):  # line:43
                if label_list[i] == image_label:  # line:44
                    sample.append(i)  # line:45
                    color_dict[i] = color_dict[sample[img_index]]  # line:46
                    break  # line:47
        random.shuffle(sample)  # line:48
        image_pair = list()  # line:50
        for img_index in range(len(sample)):  # line:51
            real_img_index = sample[img_index]  # line:52
            image_data = image_list[real_img_index]  # line:53
            image_label = label_list[real_img_index]  # line:54
            var_13 = color_dict[real_img_index]  # line:55
            read_picture.image_save(image_data, var_13, "../auto_grader/image/" + str(img_index) + ".png")  # line:57
            image_pair.append([var_13, image_label])  # line:58
        print('图片显示完毕')  # line:59
        return image_pair  # line:60

    def index(slef, row, col):  # line:62
        return row * 8 + col  # line:63

    def ui(self):  # line:65
        self.blue = '#00BFFF'  # line:66
        self.orange = 'orange'  # line:67
        self.gray = '#3d3a3a'  # line:68
        self.right_color = '#00FF00'  # line:69
        self.wrong_color = 'red'  # line:70
        self.unselected = 'white'  # line:71
        self.selected = self.orange  # line:72
        root = tk.Tk()  # line:74
        root.title(' RoboMaster 2020 Summer Camp Algorithm AutoGrader')  # line:75
        icon = PhotoImage(file="../auto_grader/favicon.ico")
        root.tk.call('wm', 'iconphoto', root._w, icon)
        # root.iconbitmap()  # line:76

        root.geometry('1000x650')  # line:77
        root["background"] = 'white'  # line:78
        root.resizable(0, 0)  # line:79
        frame1 = tk.Frame(root, bg=self.blue)  # line:81
        frame1.place(height=5, relwidth=0.25)  # line:82
        frame2 = tk.Frame(root, bg=self.orange)  # line:83
        frame2.place(relx=0.25, height=5, relwidth=0.75)  # line:84
        logo = tk.PhotoImage(file='../auto_grader/ROBOMASTER.png')  # line:86
        logo_label = tk.Label(root, image=logo, bg='white')  # line:87
        logo_label.place(x=28, y=25)  # line:88
        frame3 = tk.Frame(root, bg='white')  # line:90
        frame3.place(x=25, y=81, height=546, width=546)  # line:91
        self.score_label = tk.Label(root,
                                    bg='white',
                                    text='Score 0',
                                    fg=self.gray,
                                    bd=0,
                                    padx=0,
                                    pady=0,
                                    anchor='w',
                                    font=('Microsoft YaHei UI',
                                          32, tf.BOLD,
                                          tf.ITALIC))  # line:102
        self.score_label.place(x=626, y=15, width=306)  # line:103
        output = tk.scrolledtext.ScrolledText(root,
                                              width=70,
                                              font=('微软雅黑',
                                                    14))  # line:107
        output.place(x=622, y=87, height=530, width=328)  # line:108
        sys.stdout = text_redirector(output, 'stdout')  # line:109
        self.empty_photo = tk.PhotoImage(
            file='../auto_grader/empty.png').zoom(2)  # line:112
        self.img_button_list = list()  # line:113
        self.waitList = list()  # line:114
        for rol in range(8):  # line:115
            for col in range(8):  # line:116
                bt = tk.Button(
                    frame3,
                    bd=2,
                    bg='white',
                    state='disabled',
                    relief='flat',
                    image=self.empty_photo,
                    command=(lambda row, col: lambda: self.click_callback(row, col))(rol, col))  # line:125
                bt.grid(row=rol,
                        column=col,
                        sticky=tk.W + tk.E + tk.N + tk.S,
                        padx=3,
                        pady=3)  # line:130
                self.img_button_list.append(bt)  # line:131
        root.mainloop()  # line:132

    def load_images(self):  # line:134
        self.photoes = list()  # line:135
        for index in range(64):  # line:136
            image = tk.PhotoImage(file='../auto_grader/image/' + str(index) + '.png').zoom(2)  # line:138
            self.photoes.append(image)  # line:139
            self.img_button_list[index].config(
                image=image, state='normal')  # line:140

    def click_callback(self, row, col):  # line:142
        print(row, col)  # line:143
        index = self.index(
            row, col)  # line:144
        if [row,
            col] in self.waitList:  # line:145
            self.waitList.remove(
                [row, col])  # line:146
            self.img_button_list[index].config(
                bg=self.unselected)  # line:147
        else:  # line:148
            self.waitList.append([row, col])  # line:149
            self.img_button_list[index].config(bg=self.selected)  # line:150
            if len(self.waitList) == 2:  # line:151
                cood1 = self.waitList[1]  # line:152
                cood2 = self.waitList[0]  # line:153
                _thread.start_new_thread(self.link, (cood1[0], cood1[1], cood2[0], cood2[1]))  # line:155

    def color(self, color_num):  # line:157
        if color_num == 0:  # line:158
            return 'RED'  # line:159
        if color_num == 1:  # line:160
            return 'GREEN'  # line:161
        return 'BLUE'  # line:162

    def link(self, row1, col1,
             row2, col2):  # line:164
        index1 = self.index(row1, col1)  # line:165
        index2 = self.index(row2, col2)  # line:166
        if self.enable_ui:  # line:167
            time.sleep(0.5)  # line:168
        obj = self.ls.search(row1, col1, row2, col2)  # line:169
        if isinstance(obj, list):  # line:170
            self.current_score += self.scores[
                5]  # line:171
            print('Wrong! {0}'.format(self.scores[5]))  # line:172
            print('{0}, {1} is {2} {3}'.format(
                row1, col1,
                self.color(obj[0][0]), obj[0][1]))  # line:175
            print('{0}, {1} is {2} {3}'.format(
                row2, col2,
                self.color(obj[1][0]),
                obj[1][1]))  # line:178
            color = self.wrong_color  # line:179
        elif obj == -2:  # line:180
            self.current_score += self.scores[4]  # line:181
            print('Took more than four lines! {0}'.format(
                self.scores[4]))  # line:182
            color = self.wrong_color  # line:183
        elif obj == -1:  # line:184
            self.current_score += self.scores[6]  # line:185
            print('Invalid input! {0}'.format(self.scores[6]))  # line:186
            color = self.wrong_color  # line:187
        else:  # line:188
            self.round += 1  # line:189
            print('Round', self.round)  # line:190
            if self.round in [4, 8, 16, 27, 28, 29, 30, 31, 32]:  # line:191
                self.current_score += self.doublescores[obj - 1]  # line:192
                print('Right! +{0}'.format(
                    self.doublescores[obj - 1]))  # line:193
            else:  # line:194
                self.current_score += self.scores[obj - 1]  # line:195
                print('Right! +{0}'.format(
                    self.scores[obj - 1]))  # line:196
            color = self.right_color  # line:197
        print('Current score =',
              self.current_score)  # line:198
        print('**********************')  # line:199
        if self.enable_ui:  # line:200
            self.score_label.config(text='Score {0}'.format(
                self.current_score))  # line:201
            self.img_button_list[index1].config(
                bg=color)  # line:202
            self.img_button_list[index2].config(
                bg=color)  # line:203
            time.sleep(0.75)  # line:204
            for bt in self.img_button_list:  # line:205
                bt.config(bg=self.unselected)  # line:206
            self.waitList = []  # line:207
            if obj in [1, 2, 3, 4]:  # line:208
                self.img_button_list[index1].config(
                    image=self.empty_photo,
                    state='disabled')  # line:210
                self.img_button_list[index2].config(
                    image=self.empty_photo,
                    state='disabled')  # line:212
        return obj  # line:213


class text_redirector():  # line:216
    def __init__(self, widget, tag):  # line:217
        self.widget = widget  # line:218
        self.tag = tag  # line:219
        self.flush = sys.stdout.flush  # line:220

    def write(self, index):  # line:222
        self.widget.configure(state='normal')  # line:223
        self.widget.insert('end', index,
                           (self.tag,))  # line:224
        self.widget.see(tk.END)  # line:225
        self.widget.configure(state='disabled')  # line:226


if __name__ == "__main__":  # line:229
    ag = auto_grader()  # line:230
    input("enter to exit")
