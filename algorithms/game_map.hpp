#ifndef LINK_SEARCH_HPP
#define LINK_SEARCH_HPP

#include <vector>
#include <cstring>
#include <algorithm>
#include <bitset>
static const std::vector<int> SCORES = {50, 20, 10, 0, -10, -100, -100};
static const std::vector<int> DOUBLE_SCORES = {100, 20, 10, 0};
static std::vector<int> ans_list;

class game_map {
public:
    std::bitset<64> removed;
    int current_score;

    explicit game_map() {
        reset();
    }

    game_map(const game_map &o) = default;

    void reset() {
        removed = 0;
        current_score = 0;
    }
    int get_steps() const {
        return removed.count() >> 1;
    }


    bool validate(int row, int col) const {
        return 0 <= row && row < 8 && 0 <= col && col < 8;
    }

    bool empty(int row, int col) const {
        if (!this->validate(row, col))
            return true;
        return this->removed[row * 8 + col];
    }

    void remove(int row1, int col1, int row2, int col2) {
        this->removed[row1 * 8 + col1] = true;
        this->removed[row2 * 8 + col2] = true;
    }

    int get_score_by_result(int result) const {
        switch (result) {
            case -3: // different colors
                return SCORES[5];
            case -2: // more than 4 lines
                return SCORES[4];
            case -1: // not valid
                return SCORES[6];
            default: // 0~4 lines
                std::vector<int> bonus = {4, 8, 16, 27, 28, 29, 30, 31, 32};
                bool bonus_round = std::binary_search(bonus.begin(), bonus.end(), 1 + get_steps());
                if(bonus_round)
                    return DOUBLE_SCORES[result - 1];
                else
                    return SCORES[result - 1];
        }
    }
    int link(int row1, int col1, int row2, int col2) {
        int result = search(row1, col1, row2, col2);
        current_score += get_score_by_result(result);
        if (result >= 0)
            remove(row1, col1, row2, col2);
        return result;
    }

    int search(int row1, int col1, int row2, int col2) const {
        if (!this->validate(row1, col1) || !this->validate(row2, col2) || this->empty(row1, col1)
            || this->empty(row2, col2) || row1 == row2 && col1 == col2)
            return -1;
        int index1 = row1 * 8 + col1;
        int index2 = row2 * 8 + col2;
        if (ans_list[index1] != ans_list[index2])
            return -3;
        if (this->search_zero(row1, col1, row2, col2)) {
            return 1;
        }

        if (this->search_one(row1, col1, row2, col2)) {
            return 2;
        }

        if (this->search_two(row1, col1, row2, col2)) {
            return 3;
        }
        if (this->search_three(row1, col1, row2, col2)) {
            return 4;
        }
        return -2;
    }

    int search_zero(int row1, int col1, int row2, int col2) const {
        if (row1 != row2 && col1 != col2)
            return false;
        if (row1 == row2) {
            int left = std::min(col1, col2);
            int right = std::max(col1, col2);
            for (int i = left + 1; i < right; ++i)
                if (!this->empty(row1, i))
                    return false;
            return true;

        } else {
            int up = std::min(row1, row2);
            int down = std::max(row1, row2);
            for (int i = up + 1; i < down; ++i)
                if (!this->empty(i, col1))
                    return false;
            return true;
        }
    }

    bool search_one(int row1, int col1, int row2, int col2) const {
        if (row1 == row2 || col1 == col2)
            return false;
        if (this->empty(row1, col2) && this->search_zero(row1, col1, row1, col2) &&
            this->search_zero(row2, col2, row1, col2))
            return true;
        if (this->empty(row2, col1) && this->search_zero(row1, col1, row2, col1) &&
            this->search_zero(row2, col2, row2, col1))
            return true;
        return false;
    }

    bool search_two(int row1, int col1, int row2, int col2) const {
        for (int i = row1 - 1; i > -2; --i) {
            if (!this->empty(i, col1))
                break;
            if (this->search_one(i, col1, row2, col2))
                return true;

        }
        for (int i = row1 + 1; i < 9; ++i) {
            if (!this->empty(i, col1))
                break;
            if (this->search_one(i, col1, row2, col2))
                return true;

        }
        for (int i = col1 - 1; i > -2; --i) {

            if (!this->empty(row1, i))
                break;
            if (this->search_one(row1, i, row2, col2))
                return true;

        }
        for (int i = col1 + 1; i < 9; ++i) {
            if (!this->empty(row1, i))
                break;
            if (this->search_one(row1, i, row2, col2))
                return true;

        }
        return false;
    }

    int search_three(int row1, int col1, int row2, int col2) const {
        for (int i = row1 - 1; i > -2; --i) {
            if (!this->empty(i, col1))
                break;
            if (this->search_two(i, col1, row2, col2))
                return true;
        }
        for (int i = row1 + 1; i < 9; ++i) {
            if (!this->empty(i, col1))
                break;
            if (this->search_two(i, col1, row2, col2))
                return true;

        }
        for (int i = col1 - 1; i > -2; --i) {


            if (!this->empty(row1, i))
                break;
            if (this->search_two(row1, i, row2, col2))
                return true;
        }
        for (int i = col1 + 1; i < 9; ++i) {
            if (!this->empty(row1, i))
                break;
            if (this->search_two(row1, i, row2, col2))
                return true;

        }

        return false;
    }
};

#endif