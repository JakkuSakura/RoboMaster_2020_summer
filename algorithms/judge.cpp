//
// Created by jack on 20-8-12.
// This program is to estimate the possible highest score of a given map
//
#include "game_map.hpp"
#include "read_map.hpp"
#include <iostream>
using namespace std;

int calc() {
    int one_liner = 0, two_liner = 0;
    for (int i = 0; i < 64; ++i) {
        int r1 = i / 8, c1 = i % 8;
        for (int j = i + 1; j < 64; ++j) {
            int r2 = j / 8, c2 = j % 8;
            if (ans_list[i] != ans_list[j]) continue;
            if (r1 == r2 || c1 == c2)
                one_liner += 1;
            else
                two_liner += 1;
        }
    }
    return one_liner;
}
int main() {
    srand(time(0));
    ans_list = read_list(cin, 8 * 8);
    int one_liner = calc();
    cout << one_liner << endl;
    for (int i = 0; i < 10000000; ++i) {
        int x = rand() % 64, y = rand() % 64;
        swap(ans_list[x], ans_list[y]);
        int new_one_liner = calc();
        if (new_one_liner > one_liner)
        {
            cout << "Forward" << endl;
            cout << one_liner << endl;
            write_list(cout, ans_list);
            one_liner = new_one_liner;
        } else {
            swap(ans_list[x], ans_list[y]);
        }

    }
    return 0;
}