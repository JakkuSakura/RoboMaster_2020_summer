//
// Created by jack on 20-8-3.
//

#ifndef ALGORITHMS_READ_MAP_HPP
#define ALGORITHMS_READ_MAP_HPP

#include <vector>
#include <istream>
std::vector<int> read_list(std::istream &is, int n) {
    std::vector<int> v;
    for (int i = 0; i < n; ++i) {
        int t;
        is >> t;
        v.push_back(t);
    }
    return v;
}

#endif //ALGORITHMS_READ_MAP_HPP
