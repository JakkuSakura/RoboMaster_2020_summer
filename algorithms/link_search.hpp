#ifndef LINK_SEARCH_HPP
#define LINK_SEARCH_HPP

#include <vector>
#include

class link_search {
public
    vector<int> ans_list;
    bool grid[8][8];

    link_search(const vector<int> &ans) {
        this->ans_list = ans;
        memset(this->grid, sizeof grid, 0);
    }

    void reset( {
        memset(this->grid, sizeof grid, 0);
    }


    bool validate(int row, int col) {
        return 0 <= row && row < 8 && 0 <= col && col < 8;
    }

    bool empty(int row, int col) {
        if !this->validate(row, col)
        return true;
        return this->grid[row][col];
    }

    bool remove(row1, col1, row2, col2) {
        this->grid[row1][col1] = true;
        this->grid[row2][col2] = true;
    }

    int search(row1, col1, row2, col2) {
        if (!this->validate(row1, col1) || !this->validate(row2, col2) || this->empty(row1, col1)
            || this->empty(row2, col2) || row1 == row2 && col1 == col2)
            return -1;
        int index1 = row1 * 8 + col1;
        int index2 = row2 * 8 + col2;
        if (this->ans_list[index1] != this->ans_list[index2])
            return -3;
        if (this->search_zero(row1, col1, row2, col2))
            this->remove(row1, col1, row2, col2);
        return 1;
        if (this->search_one(row1, col1, row2, col2))
            this->remove(row1, col1, row2, col2);
        return 2;
        if (this->search_two(row1, col1, row2, col2))
            this->remove(row1, col1, row2, col2);
        return 3;
        if (this->search_three(row1, col1, row2, col2))
            this->remove(row1, col1, row2, col2);
        return 4;

        return -2;
    }

    int search_zero(row1, col1, row2, col2) {
        if (row1 != row2 && col1 != col2)
            return false;
        if (row1 == row2) {
            int left = stdmin(col1, col2);
            int right = stdmax(col1, col2);
            for (int i = left + 1; i < right; ++i)
                if !this->empty(row1, i)
            return false;
            return true;

        } else {
            int up = min(row1, row2)
            int down = max(row1, row2)
            for (int i = up + 1; i < down; ++i)
                if !this->empty(i, col1)
            return false;
            return true;
        }
    }

    bool search_one(int row1, int col1, int row2, int col2) {
        if (row1 == row2 || col1 == col2)
            return false;
        if (this->empty(row1, col2) && this->search_zero(row1, col1, row1, col2) &&
            this->search_zero(row2, col2, row1, col2))
            return true;
        if (this->empty(row2, col1) && this->search_zero(row1, col1, row2, col1) &&
            this->search_zero(row2, col2, row2, col1))
            return true;

    }

    bool search_two(int row1, int col1, int row2, int col2) {
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

    int search_three(int row1, int col1, int row2, int col2) {
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
            if this->search_two(row1, i, row2, col2)
            return true;

        }

        return false;
    }
}

#endif