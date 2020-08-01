class link_search:  #line:2
    def __init__(OO0OOOO0O0000OOOO, OOOOO00000OO0O000):  #line:3
        OO0OOOO0O0000OOOO.reset()  #line:4
        OO0OOOO0O0000OOOO.ans_list = OOOOO00000OO0O000  #line:5

    def reset(OOO0OO000OOOO0O0O):  #line:7
        OOO0OO000OOOO0O0O.grid = [[]
                                  for OOOOO0OOO000O0OOO in range(8)]  #line:8
        for O00OO0OOOOO0OO0OO in range(8):  #line:9
            for _O00O0O0000O0OO00O in range(8):  #line:10
                OOO0OO000OOOO0O0O.grid[O00OO0OOOOO0OO0OO].append(
                    False)  #line:11

    def validate(OO0O00O0OO00OOO0O, O0OOOOOO000OOOOO0,
                 OO000000O0O00OOOO):  #line:13
        return 0 <= O0OOOOOO000OOOOO0 and O0OOOOOO000OOOOO0 < 8 and 0 <= OO000000O0O00OOOO and OO000000O0O00OOOO < 8  #line:14

    def empty(O00OO000O0OO0000O, OO0OO0O0000OO000O,
              O0O00OO0OOOO0O0O0):  #line:16
        if not O00OO000O0OO0000O.validate(OO0OO0O0000OO000O,
                                          O0O00OO0OOOO0O0O0):  #line:17
            return True  #line:18
        return O00OO000O0OO0000O.grid[OO0OO0O0000OO000O][
            O0O00OO0OOOO0O0O0]  #line:19

    def remove(O0O000OOO00O0O0OO, OO0OO00O00O0OOO00, OO0O000O0O0O00OOO,
               O000OOO0O0O00OOO0, O00OOO0O0000OO0OO):  #line:21
        O0O000OOO00O0O0OO.grid[OO0OO00O00O0OOO00][
            OO0O000O0O0O00OOO] = True  #line:22
        O0O000OOO00O0O0OO.grid[O000OOO0O0O00OOO0][
            O00OOO0O0000OO0OO] = True  #line:23

    def search(OO00OOO0OO000OO0O, OO0000O00O0OO000O, O00OO00OO00O0O00O,
               O00OOO0OO00O0000O, O00OO0OO0O0OOO000):  #line:25
        if not OO00OOO0OO000OO0O.validate(
                OO0000O00O0OO000O, O00OO00OO00O0O00O
        ) or not OO00OOO0OO000OO0O.validate(
                O00OOO0OO00O0000O, O00OO0OO0O0OOO000
        ) or OO00OOO0OO000OO0O.empty(
                OO0000O00O0OO000O, O00OO00OO00O0O00O
        ) or OO00OOO0OO000OO0O.empty(
                O00OOO0OO00O0000O, O00OO0OO0O0OOO000
        ) or OO0000O00O0OO000O == O00OOO0OO00O0000O and O00OO00OO00O0O00O == O00OO0OO0O0OOO000:  #line:28
            return -1  #line:29
        OOOOOOOOO0O00O0O0 = OO0000O00O0OO000O * 8 + O00OO00OO00O0O00O  #line:30
        O00O00O0O0OOOO0O0 = O00OOO0OO00O0000O * 8 + O00OO0OO0O0OOO000  #line:31
        if OO00OOO0OO000OO0O.ans_list[
                OOOOOOOOO0O00O0O0] != OO00OOO0OO000OO0O.ans_list[
                    O00O00O0O0OOOO0O0]:  #line:32
            return [
                OO00OOO0OO000OO0O.ans_list[OOOOOOOOO0O00O0O0],
                OO00OOO0OO000OO0O.ans_list[O00O00O0O0OOOO0O0]
            ]  #line:33
        if OO00OOO0OO000OO0O.search_zero(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                         O00OOO0OO00O0000O,
                                         O00OO0OO0O0OOO000):  #line:34
            OO00OOO0OO000OO0O.remove(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                     O00OOO0OO00O0000O,
                                     O00OO0OO0O0OOO000)  #line:35
            return 1  #line:36
        if OO00OOO0OO000OO0O.search_one(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                        O00OOO0OO00O0000O,
                                        O00OO0OO0O0OOO000):  #line:37
            OO00OOO0OO000OO0O.remove(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                     O00OOO0OO00O0000O,
                                     O00OO0OO0O0OOO000)  #line:38
            return 2  #line:39
        if OO00OOO0OO000OO0O.search_two(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                        O00OOO0OO00O0000O,
                                        O00OO0OO0O0OOO000):  #line:40
            OO00OOO0OO000OO0O.remove(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                     O00OOO0OO00O0000O,
                                     O00OO0OO0O0OOO000)  #line:41
            return 3  #line:42
        if OO00OOO0OO000OO0O.search_three(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                          O00OOO0OO00O0000O,
                                          O00OO0OO0O0OOO000):  #line:43
            OO00OOO0OO000OO0O.remove(OO0000O00O0OO000O, O00OO00OO00O0O00O,
                                     O00OOO0OO00O0000O,
                                     O00OO0OO0O0OOO000)  #line:44
            return 4  #line:45
        else:  #line:46
            return -2  #line:47

    def search_zero(OO00O000O00O000O0, O0OOOOOOOOOO0000O, OO00O00OOO00OOO0O,
                    O00000OO00O0000O0, OOOO00OO000000O00):  #line:49
        if O0OOOOOOOOOO0000O != O00000OO00O0000O0 and OO00O00OOO00OOO0O != OOOO00OO000000O00:  #line:50
            return False  #line:51
        if O0OOOOOOOOOO0000O == O00000OO00O0000O0:  #line:52
            OO0OO0OO0O0000OOO = min(OO00O00OOO00OOO0O,
                                    OOOO00OO000000O00)  #line:53
            OOOO0OO0O0O0OO0OO = max(OO00O00OOO00OOO0O,
                                    OOOO00OO000000O00)  #line:54
            for O0OO0000O000OOOOO in range(OO0OO0OO0O0000OOO + 1,
                                           OOOO0OO0O0O0OO0OO):  #line:55
                if not OO00O000O00O000O0.empty(O0OOOOOOOOOO0000O,
                                               O0OO0000O000OOOOO):  #line:56
                    return False  #line:57
            return True  #line:58
        else:  #line:59
            OO0O000000O0OOOOO = min(O0OOOOOOOOOO0000O,
                                    O00000OO00O0000O0)  #line:60
            O0O00O0OOO000O0O0 = max(O0OOOOOOOOOO0000O,
                                    O00000OO00O0000O0)  #line:61
            for OOOO0O00OOO0O0000 in range(OO0O000000O0OOOOO + 1,
                                           O0O00O0OOO000O0O0):  #line:62
                if not OO00O000O00O000O0.empty(OOOO0O00OOO0O0000,
                                               OO00O00OOO00OOO0O):  #line:63
                    return False  #line:64
            return True  #line:65

    def search_one(OOO0O0O00000O0O00, OO0O000O0OO0OO0OO, OO000OOOO0OO00OOO,
                   O00O00O00OO0OO000, OO0OOOOO0O0O00000):  #line:67
        if OO0O000O0OO0OO0OO == O00O00O00OO0OO000 or OO000OOOO0OO00OOO == OO0OOOOO0O0O00000:  #line:68
            return False  #line:69
        if OOO0O0O00000O0O00.empty(
                OO0O000O0OO0OO0OO,
                OO0OOOOO0O0O00000) and OOO0O0O00000O0O00.search_zero(
                    OO0O000O0OO0OO0OO, OO000OOOO0OO00OOO, OO0O000O0OO0OO0OO,
                    OO0OOOOO0O0O00000) and OOO0O0O00000O0O00.search_zero(
                        O00O00O00OO0OO000, OO0OOOOO0O0O00000,
                        OO0O000O0OO0OO0OO, OO0OOOOO0O0O00000):  #line:70
            return True  #line:71
        if OOO0O0O00000O0O00.empty(
                O00O00O00OO0OO000,
                OO000OOOO0OO00OOO) and OOO0O0O00000O0O00.search_zero(
                    OO0O000O0OO0OO0OO, OO000OOOO0OO00OOO, O00O00O00OO0OO000,
                    OO000OOOO0OO00OOO) and OOO0O0O00000O0O00.search_zero(
                        O00O00O00OO0OO000, OO0OOOOO0O0O00000,
                        O00O00O00OO0OO000, OO000OOOO0OO00OOO):  #line:72
            return True  #line:73

    def search_two(OO00OOOO0OOO0000O, OOOOOO00O0OO00O0O, O0O000O0OOO0OOO0O,
                   O0000O0O0O000OOO0, OOO0OOO00O0000O0O):  #line:75
        for O00O0O0O000OO0O00 in range(OOOOOO00O0OO00O0O - 1, -2,
                                       -1):  #line:76
            if not OO00OOOO0OOO0000O.empty(O00O0O0O000OO0O00,
                                           O0O000O0OOO0OOO0O):  #line:77
                break  #line:78
            if OO00OOOO0OOO0000O.search_one(O00O0O0O000OO0O00,
                                            O0O000O0OOO0OOO0O,
                                            O0000O0O0O000OOO0,
                                            OOO0OOO00O0000O0O):  #line:79
                return True  #line:80
        for O00O0O0O000OO0O00 in range(OOOOOO00O0OO00O0O + 1, 9):  #line:81
            if not OO00OOOO0OOO0000O.empty(O00O0O0O000OO0O00,
                                           O0O000O0OOO0OOO0O):  #line:82
                break  #line:83
            if OO00OOOO0OOO0000O.search_one(O00O0O0O000OO0O00,
                                            O0O000O0OOO0OOO0O,
                                            O0000O0O0O000OOO0,
                                            OOO0OOO00O0000O0O):  #line:84
                return True  #line:85
        for OO000O0O0O0O000O0 in range(O0O000O0OOO0OOO0O - 1, -2,
                                       -1):  #line:86
            if not OO00OOOO0OOO0000O.empty(OOOOOO00O0OO00O0O,
                                           OO000O0O0O0O000O0):  #line:87
                break  #line:88
            if OO00OOOO0OOO0000O.search_one(OOOOOO00O0OO00O0O,
                                            OO000O0O0O0O000O0,
                                            O0000O0O0O000OOO0,
                                            OOO0OOO00O0000O0O):  #line:89
                return True  #line:90
        for OO000O0O0O0O000O0 in range(O0O000O0OOO0OOO0O + 1, 9):  #line:91
            if not OO00OOOO0OOO0000O.empty(OOOOOO00O0OO00O0O,
                                           OO000O0O0O0O000O0):  #line:92
                break  #line:93
            if OO00OOOO0OOO0000O.search_one(OOOOOO00O0OO00O0O,
                                            OO000O0O0O0O000O0,
                                            O0000O0O0O000OOO0,
                                            OOO0OOO00O0000O0O):  #line:94
                return True  #line:95
        return False  #line:96

    def search_three(OOO00000O000O0000, OO00O00O00O00OO00, OO0OO0OO000O0OO0O,
                     O000000O0OOOOOO00, O0O0OO00000OOO0OO):  #line:98
        for OO0O0OOO0O00OO00O in range(OO00O00O00O00OO00 - 1, -2,
                                       -1):  #line:99
            if not OOO00000O000O0000.empty(OO0O0OOO0O00OO00O,
                                           OO0OO0OO000O0OO0O):  #line:100
                break  #line:101
            if OOO00000O000O0000.search_two(OO0O0OOO0O00OO00O,
                                            OO0OO0OO000O0OO0O,
                                            O000000O0OOOOOO00,
                                            O0O0OO00000OOO0OO):  #line:102
                return True  #line:103
        for OO0O0OOO0O00OO00O in range(OO00O00O00O00OO00 + 1, 9):  #line:104
            if not OOO00000O000O0000.empty(OO0O0OOO0O00OO00O,
                                           OO0OO0OO000O0OO0O):  #line:105
                break  #line:106
            if OOO00000O000O0000.search_two(OO0O0OOO0O00OO00O,
                                            OO0OO0OO000O0OO0O,
                                            O000000O0OOOOOO00,
                                            O0O0OO00000OOO0OO):  #line:107
                return True  #line:108
        for OOOO00O0O00OOO000 in range(OO0OO0OO000O0OO0O - 1, -2,
                                       -1):  #line:109
            if not OOO00000O000O0000.empty(OO00O00O00O00OO00,
                                           OOOO00O0O00OOO000):  #line:110
                break  #line:111
            if OOO00000O000O0000.search_two(OO00O00O00O00OO00,
                                            OOOO00O0O00OOO000,
                                            O000000O0OOOOOO00,
                                            O0O0OO00000OOO0OO):  #line:112
                return True  #line:113
        for OOOO00O0O00OOO000 in range(OO0OO0OO000O0OO0O + 1, 9):  #line:114
            if not OOO00000O000O0000.empty(OO00O00O00O00OO00,
                                           OOOO00O0O00OOO000):  #line:115
                break  #line:116
            if OOO00000O000O0000.search_two(OO00O00O00O00OO00,
                                            OOOO00O0O00OOO000,
                                            O000000O0OOOOOO00,
                                            O0O0OO00000OOO0OO):  #line:117
                return True  #line:118
        return False  #line:119
