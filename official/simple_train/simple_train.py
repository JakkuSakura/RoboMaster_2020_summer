import numpy as np

class simple_train_one_num:
    #初始化， 传入的参数为 data： 训练的数据集， 训练的标签集， 训练的容忍值， 系数步进值， 截距步进值
    def __init__(self, data, labels, toler, step_w, step_b):
        self.train_data = data #训练数据集
        self.train_label = labels #训练的标签集
        self.toler = toler #容忍值
        self.step_w = step_w #系数步进值
        self.step_b = step_b #截距步进值
        self.num_kind = self.label_rank_num(self.train_label) #计算标准集中的有的数字种类个数
        self.train_data_dim = int(np.shape(self.train_data)[1])
        
        #根据数字种类个数，计算训练矩阵个数， 进行两两分组， 例如有1,2,3数字， 即有3种数字，那么训练矩阵包括 1,2的矩阵， 1,3的矩阵， 2,3的矩阵 共3*(3-1)/2 = 3个矩阵
        self.w = np.zeros((int(len(self.num_kind) * (len(self.num_kind) - 1) / 2), self.train_data_dim) )
        self.b = np.zeros((int(len(self.num_kind) * (len(self.num_kind) - 1) / 2), 1))
    #计算标签集中的数字种类
    def label_rank_num(self, label):
        rank = []
        for i in label:
            flag = False
            #遍历rank， 找到没有的数字
            for j in rank:
                if j == i:
                   flag = True
            #添加没有的数字
            if flag == False:
                 rank.append(i)
        return rank
    #训练两个数字的区分
    def train_learn_two_num(self, i, j):
        #申明矩阵和截距
        w = np.zeros(np.shape(self.train_data)[1])
        b = 0
        #用于判断是否所有标签都可以判断正确
        train_flag = 1
        while train_flag != 0:
            train_flag = 0
            
            num = 0
            #循环所有的标签
            while num < len(self.train_label):
                y = 0
                #判断是第一个数字还是第二个数字
                if self.train_label[num] == self.num_kind[i]:
                    y = 1
                elif self.train_label[num] == self.num_kind[j]:
                    y = -1
                
                if y != 0:
                    #计算模型值
                    if (y * np.dot(w.T, self.train_data[num]) + b) <= self.toler:
                        w += self.step_w * self.train_data[num] * y
                        b += self.step_b * y
                        train_flag = 1
                num+=1
        return w,b
    def train_learn(self):
        num = 0
        num_len = len(self.num_kind)
        #循环所有数字的组合
        i = 0
        while i < num_len:
            j = i+1
            while j < num_len:
                #训练两个数字
                self.w[num], self.b[num] = self.train_learn_two_num(i, j)
                j+=1
                num+=1
            i+=1
        
    def predict(self, test_data):
        ans = []
        num_len = len(self.num_kind)
        for i in test_data:
            #计算每两种数字的组合，再根据判断出数字出现次数最多的最终预测结果
            test_ans = np.zeros(num_len)
            
            num_i = 0
            
            num = 0
            #遍历所有数字组合
            while num_i < num_len:
                num_j = num_i + 1
                while num_j < num_len:
                    #计算两个数的判断，大于0为第一数， 小于为第二数
                    if (np.dot(self.w[num].T, i) + self.b[num]) > 0:
                        #给对应的数计票
                        test_ans[num_i]+=1
                    else:
                        #给对应的数计票
                        test_ans[num_j]+=1
                    num_j+=1
                    num+=1
                num_i+=1
            #统计所有的投票，看哪个数字最多
            num_i = 0
            ans_max = -1
            ans_i = -1
            while num_i < num_len:
                if ans_max < test_ans[num_i]:
                    ans_max = test_ans[num_i]
                    ans_i = num_i
                num_i+=1
            ans.append(self.num_kind[ans_i])
        ans = np.array(ans)
        return ans
        


if __name__ == "__main__":
    import sys
    sys.path.append("../read_picture/")
    import read_picture
    
    train_image, train_label = read_picture.read_image_data('../../mnist_data/train-images.idx3-ubyte', '../../mnist_data/train-labels.idx1-ubyte')
    
    train_image_vector = np.reshape(train_image, (60000, 784))
    
    simple_train = simple_train_one_num(train_image_vector[0:5000], train_label[0:5000], 10, 0.1, 2.55)
    
    simple_train.train_learn()
    
    #构造测试集
    test_image_vector = train_image_vector[5000:5100]
    test_ans = train_label[5000:5100]
    #计算预测
    pre_ans = simple_train.predict(test_image_vector)
    
    #计算正确率
    i = 0
    true_num = 0
    while i < len(test_image_vector):
        if test_ans[i] ==  pre_ans[i]:
            true_num += 1
        i+=1
    print(true_num/i)
    
    

