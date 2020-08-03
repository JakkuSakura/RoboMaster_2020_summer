class link_search:  # line:2
    def __init__(self, ans):  # line:3
        self.reset()  # line:4
        self.ans_list = ans  # line:5

    def reset(self):  # line:7
        self.grid = [[] for _ in range(8)]  # line:8
        for i in range(8):  # line:9
            for j in range(8):  # line:10
                self.grid[i].append(False)  # line:11

    def validate(self, row, col):  # line:13
        return 0 <= row < 8 and 0 <= col < 8  # line:14

    def empty(self, row, col):  # line:16
        if not self.validate(row, col):  # line:17
            return True  # line:18
        return self.grid[row][col]  # line:19

    def remove(self, row1, col1, row2, col2):  # line:21
        self.grid[row1][col1] = True  # line:22
        self.grid[row2][col2] = True  # line:23

    def search(self, row1, col1, row2, col2):  # line:25
        if not self.validate(row1, col1) or not self.validate(row2, col2) or self.empty(row1, col1) or self.empty(row2,
                                                                                                                  col2) or row1 == row2 and col1 == col2:  # line:28
            return -1  # line:29
        index1 = row1 * 8 + col1  # line:30
        index2 = row2 * 8 + col2  # line:31
        if self.ans_list[index1] != self.ans_list[index2]:  # line:32
            # Do not match
            return [self.ans_list[index1], self.ans_list[index2]]  # line:33
        if self.search_zero(row1, col1, row2, col2):  # line:34
            self.remove(row1, col1, row2, col2)  # line:35
            return 1  # line:36
        if self.search_one(row1, col1, row2, col2):  # line:37
            self.remove(row1, col1, row2, col2)  # line:38
            return 2  # line:39
        if self.search_two(row1, col1, row2, col2):  # line:40
            self.remove(row1, col1, row2, col2)  # line:41
            return 3  # line:42
        if self.search_three(row1, col1, row2, col2):  # line:43
            self.remove(row1, col1, row2, col2)  # line:44
            return 4  # line:45
        else:  # line:46
            # Unreachable or more turns
            return -2  # line:47

    def search_zero(self, row1, col1, row2, col2):  # line:49
        if row1 != row2 and col1 != col2:  # line:50
            return False  # line:51
        if row1 == row2:  # line:52
            left = min(col1, col2)  # line:53
            right = max(col1, col2)  # line:54
            for i in range(left + 1, right):  # line:55
                if not self.empty(row1, i):  # line:56
                    return False  # line:57
            return True  # line:58
        else:  # line:59
            up = min(row1, row2)  # line:60
            down = max(row1, row2)  # line:61
            for i in range(up + 1, down):  # line:62
                if not self.empty(i, col1):  # line:63
                    return False  # line:64
            return True  # line:65

    def search_one(self, row1, col1, row2, col2):  # line:67
        if row1 == row2 or col1 == col2:  # line:68
            return False  # line:69
        if self.empty(row1, col2) and self.search_zero(row1, col1, row1, col2) \
                and self.search_zero(row2, col2, row1, col2):  # line:70
            return True  # line:71
        if self.empty(row2, col1) and self.search_zero(row1, col1, row2, col1) \
                and self.search_zero(row2, col2, row2, col1):  # line:72
            return True  # line:73
        return False

    def search_two(self, row1, col1, row2, col2):  # line:75
        for i in range(row1 - 1, -2, -1):  # line:76
            if not self.empty(i, col1):  # line:77
                break  # line:78
            if self.search_one(i, col1, row2, col2):  # line:79
                return True  # line:80
        for i in range(row1 + 1, 9):  # line:81
            if not self.empty(i, col1):  # line:82
                break  # line:83
            if self.search_one(i, col1, row2, col2):  # line:84
                return True  # line:85
        for i in range(col1 - 1, -2, -1):  # line:86
            if not self.empty(row1, i):  # line:87
                break  # line:88
            if self.search_one(row1, i, row2, col2):  # line:89
                return True  # line:90
        for i in range(col1 + 1, 9):  # line:91
            if not self.empty(row1, i):  # line:92
                break  # line:93
            if self.search_one(row1, i, row2, col2):  # line:94
                return True  # line:95
        return False  # line:96

    def search_three(self, row1, col1, row2, col2):  # line:98
        for i in range(row1 - 1, -2, -1):  # line:99
            if not self.empty(i, col1):  # line:100
                break  # line:101
            if self.search_two(i, col1, row2, col2):  # line:102
                return True  # line:103
        for i in range(row1 + 1, 9):  # line:104
            if not self.empty(i, col1):  # line:105
                break  # line:106
            if self.search_two(i, col1, row2, col2):  # line:107
                return True  # line:108
        for i in range(col1 - 1, -2, -1):  # line:109
            if not self.empty(row1, i):  # line:110
                break  # line:111
            if self.search_two(row1, i, row2, col2):  # line:112
                return True  # line:113
        for i in range(col1 + 1, 9):  # line:114
            if not self.empty(row1, i):  # line:115
                break  # line:116
            if self.search_two(row1, i, row2, col2):  # line:117
                return True  # line:118
        return False  # line:119
