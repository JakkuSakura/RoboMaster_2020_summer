import os  #line:1
import sys  #line:2
import time  #line:3
import random  #line:4
import _thread  #line:5
import tkinter as tk  #line:6
import tkinter.font as tf  #line:7
import tkinter.scrolledtext  #line:8
from PIL.ImageTk import PhotoImage
from link_search import link_search  #line:9
sys.path.append("../read_picture/")  #line:10
import read_picture  #line:11


class auto_grader:  #line:14
    def __init__(O0OO000O0OO0O0OOO, enable_ui=True):  #line:15
        if enable_ui:  #line:16
            _thread.start_new_thread(O0OO000O0OO0O0OOO.ui, tuple())  #line:17
            time.sleep(1)  #line:18
        O000OO00OOO0OO0OO = '../mnist_data/t10k-images.idx3-ubyte'  #line:19
        O0O00OOOO00O00OO0 = '../mnist_data/t10k-labels.idx1-ubyte'  #line:20
        O0OO000OOO0O0O000 = O0OO000O0OO0O0OOO.random_image(
            O000OO00OOO0OO0OO, O0O00OOOO00O00OO0)  #line:21
        O0OO000O0OO0O0OOO.load_images()  #line:22
        O0OO000O0OO0O0OOO.ls = link_search(O0OO000OOO0O0O000)  #line:23
        O0OO000O0OO0O0OOO.scores = [50, 20, 10, 0, -10, -100, -100]  #line:24
        O0OO000O0OO0O0OOO.doublescores = [100, 20, 10, 0]  #line:25
        O0OO000O0OO0O0OOO.__O00O00O0OO00000OO = 0  #line:27
        O0OO000O0OO0O0OOO.round = 0  #line:28
        O0OO000O0OO0O0OOO.enable_ui = enable_ui  #line:29

    def random_image(O000O0OOO0OOOO000, O0OOOO00OO0O00000,
                     OOO0OOO0OO00000OO):  #line:31
        OO00OOO00OO00O0O0, O0000O000000O000O = read_picture.read_image_data(
            O0OOOO00OO0O00000, OOO0OOO0OO00000OO)  #line:33
        O00O000O00000O00O = random.sample(range(0, len(OO00OOO00OO00O0O0)),
                                          32)  #line:34
        print('随机取样完成')  #line:35
        O0OOO00OO0O00O000 = dict()  #line:36
        for OO0OO0OOOO0OOO0OO in O00O000O00000O00O:  #line:37
            O0OOO00OO0O00O000[OO0OO0OOOO0OOO0OO] = random.randint(0,
                                                                  2)  #line:38
        for O0000O0O0O0O000O0 in range(len(O00O000O00000O00O)):  #line:39
            OOO0O000000O000OO = O0000O000000O000O[
                O00O000O00000O00O[O0000O0O0O0O000O0]]  #line:40
            for OOO0000OOO0OOOO00 in range(
                    random.randint(0,
                                   len(OO00OOO00OO00O0O0) // 2),
                    len(OO00OOO00OO00O0O0)):  #line:43
                if O0000O000000O000O[
                        OOO0000OOO0OOOO00] == OOO0O000000O000OO and OOO0000OOO0OOOO00 not in O0OOO00OO0O00O000:  #line:44
                    O00O000O00000O00O.append(OOO0000OOO0OOOO00)  #line:45
                    O0OOO00OO0O00O000[OOO0000OOO0OOOO00] = O0OOO00OO0O00O000[
                        O00O000O00000O00O[O0000O0O0O0O000O0]]  #line:46
                    break  #line:47
        random.shuffle(O00O000O00000O00O)  #line:48
        OO00O0O00O0OO0OOO = list()  #line:50
        for O0000O0O0O0O000O0 in range(len(O00O000O00000O00O)):  #line:51
            OO0OO0OOOO0OOO0OO = O00O000O00000O00O[O0000O0O0O0O000O0]  #line:52
            OO00OOO0OO00OOOOO = OO00OOO00OO00O0O0[OO0OO0OOOO0OOO0OO]  #line:53
            OOO0O000000O000OO = O0000O000000O000O[OO0OO0OOOO0OOO0OO]  #line:54
            O000000O00O0OO0O0 = O0OOO00OO0O00O000[OO0OO0OOOO0OOO0OO]  #line:55
            read_picture.image_save(OO00OOO0OO00OOOOO, O000000O00O0OO0O0,
                                    "../auto_grader/image/" +
                                    str(O0000O0O0O0O000O0) + ".png")  #line:57
            OO00O0O00O0OO0OOO.append([O000000O00O0OO0O0,
                                      OOO0O000000O000OO])  #line:58
        print('图片显示完毕')  #line:59
        return OO00O0O00O0OO0OOO  #line:60

    def index(OOOOO0O00000O0000, O0OO000OOOOO000O0,
              O0OO00OOO0000OOOO):  #line:62
        return O0OO000OOOOO000O0 * 8 + O0OO00OOO0000OOOO  #line:63

    def ui(OOO00O000OO00OOOO):  #line:65
        OOO00O000OO00OOOO.blue = '#00BFFF'  #line:66
        OOO00O000OO00OOOO.orange = 'orange'  #line:67
        OOO00O000OO00OOOO.gray = '#3d3a3a'  #line:68
        OOO00O000OO00OOOO.right_color = '#00FF00'  #line:69
        OOO00O000OO00OOOO.wrong_color = 'red'  #line:70
        OOO00O000OO00OOOO.unselected = 'white'  #line:71
        OOO00O000OO00OOOO.selected = OOO00O000OO00OOOO.orange  #line:72
        OOOOO00O0O00O00O0 = tk.Tk()  #line:74
        OOOOO00O0O00O00O0.title(
            ' RoboMaster 2020 Summer Camp Algorithm AutoGrader')  #line:75
        icon = PhotoImage(file="../auto_grader/favicon.ico")
        OOOOO00O0O00O00O0.tk.call('wm', 'iconphoto', OOOOO00O0O00O00O0._w, icon)
        # OOOOO00O0O00O00O0.iconbitmap('../auto_grader/favicon.ico')  #line:76
        OOOOO00O0O00O00O0.geometry('1000x650')  #line:77
        OOOOO00O0O00O00O0["background"] = 'white'  #line:78
        OOOOO00O0O00O00O0.resizable(0, 0)  #line:79
        O00OOOOOO00OO00O0 = tk.Frame(OOOOO00O0O00O00O0,
                                     bg=OOO00O000OO00OOOO.blue)  #line:81
        O00OOOOOO00OO00O0.place(height=5, relwidth=0.25)  #line:82
        O000OOOO000OO0O0O = tk.Frame(OOOOO00O0O00O00O0,
                                     bg=OOO00O000OO00OOOO.orange)  #line:83
        O000OOOO000OO0O0O.place(relx=0.25, height=5, relwidth=0.75)  #line:84
        O000OO0OO00O00000 = tk.PhotoImage(
            file='../auto_grader/ROBOMASTER.png')  #line:86
        OO0OOO0OOOO0O00OO = tk.Label(OOOOO00O0O00O00O0,
                                     image=O000OO0OO00O00000,
                                     bg='white')  #line:87
        OO0OOO0OOOO0O00OO.place(x=28, y=25)  #line:88
        O0O00OO0O0O000O00 = tk.Frame(OOOOO00O0O00O00O0, bg='white')  #line:90
        O0O00OO0O0O000O00.place(x=25, y=81, height=546, width=546)  #line:91
        OOO00O000OO00OOOO.score_label = tk.Label(OOOOO00O0O00O00O0,
                                                 bg='white',
                                                 text='Score 0',
                                                 fg=OOO00O000OO00OOOO.gray,
                                                 bd=0,
                                                 padx=0,
                                                 pady=0,
                                                 anchor='w',
                                                 font=('Microsoft YaHei UI',
                                                       32, tf.BOLD,
                                                       tf.ITALIC))  #line:102
        OOO00O000OO00OOOO.score_label.place(x=626, y=15, width=306)  #line:103
        OO0O000OO0O00O0O0 = tk.scrolledtext.ScrolledText(OOOOO00O0O00O00O0,
                                                         width=70,
                                                         font=('微软雅黑',
                                                               14))  #line:107
        OO0O000OO0O00O0O0.place(x=622, y=87, height=530, width=328)  #line:108
        sys.stdout = text_redirector(OO0O000OO0O00O0O0, 'stdout')  #line:109
        OOO00O000OO00OOOO.empty_photo = tk.PhotoImage(
            file='../auto_grader/empty.png').zoom(2)  #line:112
        OOO00O000OO00OOOO.img_button_list = list()  #line:113
        OOO00O000OO00OOOO.waitList = list()  #line:114
        for OO0OOOOOOOO000O0O in range(8):  #line:115
            for O0O000OOO0OO00O00 in range(8):  #line:116
                OO00000O0OO00OOOO = tk.Button(
                    O0O00OO0O0O000O00,
                    bd=2,
                    bg='white',
                    state='disabled',
                    relief='flat',
                    image=OOO00O000OO00OOOO.empty_photo,
                    command=(lambda OOO0O00O00O0OOO00, O0OO0OOOO00OOO000:
                             lambda: OOO00O000OO00OOOO.click_callback(
                                 OOO0O00O00O0OOO00, O0OO0OOOO00OOO000))(
                                     OO0OOOOOOOO000O0O,
                                     O0O000OOO0OO00O00))  #line:125
                OO00000O0OO00OOOO.grid(row=OO0OOOOOOOO000O0O,
                                       column=O0O000OOO0OO00O00,
                                       sticky=tk.W + tk.E + tk.N + tk.S,
                                       padx=3,
                                       pady=3)  #line:130
                OOO00O000OO00OOOO.img_button_list.append(
                    OO00000O0OO00OOOO)  #line:131
        OOOOO00O0O00O00O0.mainloop()  #line:132

    def load_images(O0OOOO000O0OOO000):  #line:134
        O0OOOO000O0OOO000.photoes = list()  #line:135
        for OO0O0O0O0OOO0OOOO in range(64):  #line:136
            O0000O00000O0OOOO = tk.PhotoImage(file='../auto_grader/image/' +
                                              str(OO0O0O0O0OOO0OOOO) +
                                              '.png').zoom(2)  #line:138
            O0OOOO000O0OOO000.photoes.append(O0000O00000O0OOOO)  #line:139
            O0OOOO000O0OOO000.img_button_list[OO0O0O0O0OOO0OOOO].config(
                image=O0000O00000O0OOOO, state='normal')  #line:140

    def click_callback(O00OO0OO0OOO00000, OO0O00OO0OO000OOO,
                       OOOO0OO0OOO0OO00O):  #line:142
        print(OO0O00OO0OO000OOO, OOOO0OO0OOO0OO00O)  #line:143
        OO00O0OOOO0O00000 = O00OO0OO0OOO00000.index(
            OO0O00OO0OO000OOO, OOOO0OO0OOO0OO00O)  #line:144
        if [OO0O00OO0OO000OOO,
                OOOO0OO0OOO0OO00O] in O00OO0OO0OOO00000.waitList:  #line:145
            O00OO0OO0OOO00000.waitList.remove(
                [OO0O00OO0OO000OOO, OOOO0OO0OOO0OO00O])  #line:146
            O00OO0OO0OOO00000.img_button_list[OO00O0OOOO0O00000].config(
                bg=O00OO0OO0OOO00000.unselected)  #line:147
        else:  #line:148
            O00OO0OO0OOO00000.waitList.append(
                [OO0O00OO0OO000OOO, OOOO0OO0OOO0OO00O])  #line:149
            O00OO0OO0OOO00000.img_button_list[OO00O0OOOO0O00000].config(
                bg=O00OO0OO0OOO00000.selected)  #line:150
            if (len(O00OO0OO0OOO00000.waitList) == 2):  #line:151
                OO0O00OOOO0O0O0O0 = O00OO0OO0OOO00000.waitList[1]  #line:152
                OO0O0O000OOOOO000 = O00OO0OO0OOO00000.waitList[0]  #line:153
                _thread.start_new_thread(
                    O00OO0OO0OOO00000.link,
                    (OO0O00OOOO0O0O0O0[0], OO0O00OOOO0O0O0O0[1],
                     OO0O0O000OOOOO000[0], OO0O0O000OOOOO000[1]))  #line:155

    def color(OO00000OO0OO0O000, OO0OOOO0O00O000O0):  #line:157
        if OO0OOOO0O00O000O0 == 0:  #line:158
            return 'RED'  #line:159
        if OO0OOOO0O00O000O0 == 1:  #line:160
            return 'GREEN'  #line:161
        return 'BLUE'  #line:162

    def link(OO0O0OOO00OO0OOOO, OOO0OOO0O00O00000, OO000OOOOO00O0O00,
             OOOO00O00O0O00O0O, O0O0000O0000OO00O):  #line:164
        OO00OOO0O00O00O0O = OO0O0OOO00OO0OOOO.index(
            OOO0OOO0O00O00000, OO000OOOOO00O0O00)  #line:165
        O0OO00O0OO00O0OOO = OO0O0OOO00OO0OOOO.index(
            OOOO00O00O0O00O0O, O0O0000O0000OO00O)  #line:166
        if OO0O0OOO00OO0OOOO.enable_ui:  #line:167
            time.sleep(0.5)  #line:168
        O0O0OOOO0OO0000O0 = OO0O0OOO00OO0OOOO.ls.search(
            OOO0OOO0O00O00000, OO000OOOOO00O0O00, OOOO00O00O0O00O0O,
            O0O0000O0000OO00O)  #line:169
        if isinstance(O0O0OOOO0OO0000O0, list):  #line:170
            OO0O0OOO00OO0OOOO.__O00O00O0OO00000OO += OO0O0OOO00OO0OOOO.scores[
                5]  #line:171
            print('Wrong! {0}'.format(OO0O0OOO00OO0OOOO.scores[5]))  #line:172
            print('{0}, {1} is {2} {3}'.format(
                OOO0OOO0O00O00000, OO000OOOOO00O0O00,
                OO0O0OOO00OO0OOOO.color(O0O0OOOO0OO0000O0[0][0]),
                O0O0OOOO0OO0000O0[0][1]))  #line:175
            print('{0}, {1} is {2} {3}'.format(
                OOOO00O00O0O00O0O, O0O0000O0000OO00O,
                OO0O0OOO00OO0OOOO.color(O0O0OOOO0OO0000O0[1][0]),
                O0O0OOOO0OO0000O0[1][1]))  #line:178
            O000O0OOOO00000O0 = OO0O0OOO00OO0OOOO.wrong_color  #line:179
        elif O0O0OOOO0OO0000O0 == -2:  #line:180
            OO0O0OOO00OO0OOOO.__O00O00O0OO00000OO += OO0O0OOO00OO0OOOO.scores[
                4]  #line:181
            print('Took more than four lines! {0}'.format(
                OO0O0OOO00OO0OOOO.scores[4]))  #line:182
            O000O0OOOO00000O0 = OO0O0OOO00OO0OOOO.wrong_color  #line:183
        elif O0O0OOOO0OO0000O0 == -1:  #line:184
            OO0O0OOO00OO0OOOO.__O00O00O0OO00000OO += OO0O0OOO00OO0OOOO.scores[
                6]  #line:185
            print('Invalid input! {0}'.format(
                OO0O0OOO00OO0OOOO.scores[6]))  #line:186
            O000O0OOOO00000O0 = OO0O0OOO00OO0OOOO.wrong_color  #line:187
        else:  #line:188
            OO0O0OOO00OO0OOOO.round += 1  #line:189
            print('Round', OO0O0OOO00OO0OOOO.round)  #line:190
            if OO0O0OOO00OO0OOOO.round in [4, 8, 16, 27, 28, 29, 30, 31,
                                           32]:  #line:191
                OO0O0OOO00OO0OOOO.__O00O00O0OO00000OO += OO0O0OOO00OO0OOOO.doublescores[
                    O0O0OOOO0OO0000O0 - 1]  #line:192
                print('Right! +{0}'.format(
                    OO0O0OOO00OO0OOOO.doublescores[O0O0OOOO0OO0000O0 -
                                                   1]))  #line:193
            else:  #line:194
                OO0O0OOO00OO0OOOO.__O00O00O0OO00000OO += OO0O0OOO00OO0OOOO.scores[
                    O0O0OOOO0OO0000O0 - 1]  #line:195
                print('Right! +{0}'.format(
                    OO0O0OOO00OO0OOOO.scores[O0O0OOOO0OO0000O0 -
                                             1]))  #line:196
            O000O0OOOO00000O0 = OO0O0OOO00OO0OOOO.right_color  #line:197
        print('Current score =',
              OO0O0OOO00OO0OOOO.__O00O00O0OO00000OO)  #line:198
        print('**********************')  #line:199
        if OO0O0OOO00OO0OOOO.enable_ui:  #line:200
            OO0O0OOO00OO0OOOO.score_label.config(text='Score {0}'.format(
                OO0O0OOO00OO0OOOO.__O00O00O0OO00000OO))  #line:201
            OO0O0OOO00OO0OOOO.img_button_list[OO00OOO0O00O00O0O].config(
                bg=O000O0OOOO00000O0)  #line:202
            OO0O0OOO00OO0OOOO.img_button_list[O0OO00O0OO00O0OOO].config(
                bg=O000O0OOOO00000O0)  #line:203
            time.sleep(0.75)  #line:204
            for OOO0O0OOOOOOOOO0O in OO0O0OOO00OO0OOOO.img_button_list:  #line:205
                OOO0O0OOOOOOOOO0O.config(
                    bg=OO0O0OOO00OO0OOOO.unselected)  #line:206
            OO0O0OOO00OO0OOOO.waitList = []  #line:207
            if O0O0OOOO0OO0000O0 in [1, 2, 3, 4]:  #line:208
                OO0O0OOO00OO0OOOO.img_button_list[OO00OOO0O00O00O0O].config(
                    image=OO0O0OOO00OO0OOOO.empty_photo,
                    state='disabled')  #line:210
                OO0O0OOO00OO0OOOO.img_button_list[O0OO00O0OO00O0OOO].config(
                    image=OO0O0OOO00OO0OOOO.empty_photo,
                    state='disabled')  #line:212
        return O0O0OOOO0OO0000O0  #line:213


class text_redirector():  #line:216
    def __init__(O00OO0O0000OOOOOO, OOO000O000000000O,
                 OO00000OOO000000O):  #line:217
        O00OO0O0000OOOOOO.widget = OOO000O000000000O  #line:218
        O00OO0O0000OOOOOO.tag = OO00000OOO000000O  #line:219
        O00OO0O0000OOOOOO.flush = sys.stdout.flush  #line:220

    def write(OO00O00O000O0O0OO, OO0O0O00O00O00OOO):  #line:222
        OO00O00O000O0O0OO.widget.configure(state='normal')  #line:223
        OO00O00O000O0O0OO.widget.insert('end', OO0O0O00O00O00OOO,
                                        (OO00O00O000O0O0OO.tag, ))  #line:224
        OO00O00O000O0O0OO.widget.see(tk.END)  #line:225
        OO00O00O000O0O0OO.widget.configure(state='disabled')  #line:226


if __name__ == "__main__":  #line:229
    ag = auto_grader()  #line:230
    input('enter to exit')  #line:231
