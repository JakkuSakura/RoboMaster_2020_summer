RoboMaster 2020 Summer Camp AutoGrader readme

Python version 3.x required
numpy, PIL required

0.直接双击开打 auto_grader.py 即可游玩连连看游戏

1.在代码中导入 auto_grader 文件中的 auto_grader 类
例: import os
    import sys
    sys.path.append("../auto_grader/") # 将路径修改为 auto_grader 所在目录
    from auto_grader import auto_grader

2.在代码中声明 auto_grader 类的实例
    构造函数参数 enable_ui： 表示是否开启UI，默认为True
    在开启UI的情况下每次连接延时0.75s，信息输出到UI窗口
    在不开启UI的情况下无延时，用于调试，信息直接向命令行窗口输出
    代码提交给助教时必须开启UI模式
例: ag = auto_grader(False) # 不开启UI

3.在 auto_grader/image 路径下读取图片进行识别，图片名称依次为 0.png, 1.png, ... , 63.png

4.调用 link(r1, c1, r2, c2) 进行连连看
    参数：ri, ci 表示第i个点的行数、列数
    返回值：1) 若两个点表示的颜色和数字不一致，则返回一个列表[[COLOR1, NUM1], [COLOR2, NUM2]]
               表示正确的识别结果，例如[[0, 9], [2, 5]]，其中RED为0，GREEN为1，BLUE为2
            2) 若传入的值非法，则返回-1
            3) 若需要连接直线的条数大于4条，则返回-2
            4) 能够正常消除，则返回所用直线的条数
例: result = ag.link(0, 0, 1, 1)

5.在程序结束后调用 os.system('pause')
    若未调用该函数导致UI窗口消失、成绩未记录等情况责任自负

Warning: 请不要尝试修改auto_grader类中的内容，一旦发现取消成绩