#include "game_map.hpp"
#include "read_map.hpp"
#include <set>
#include <unordered_map>
#include <iostream>
#include <thread>

using namespace std;
struct step {
    int o1, o2;
};
struct state {
    game_map map;
    std::vector<step> steps;
    int val = 0;
};


struct comp_state {
    int factor;

    inline int get_val(int current_score, int steps) const {
        return current_score - steps * factor;
    }

    inline int get_val(const state &s) const {
        return get_val(s.map.current_score, s.map.get_steps());
    }

    inline bool operator()(const state &lhs, const state &rhs) const {
        return lhs.val > rhs.val;
    }

};

state pop_best_state(multiset<state, comp_state> &qu) {
    auto it = qu.begin();
    auto x = *it;
    qu.erase(it);
    return x;
}

state pop_worst_state(multiset<state, comp_state> &qu) {
    auto it = --qu.end();
    auto x = *it;
    qu.erase(it);
    return x;
}

void show_ans(ostream &os, const state &s) {
    char buf[256];
    os << "score: " << s.map.current_score << " ";
    for (auto step : s.steps) {
        int r1 = step.o1 / 8, c1 = step.o1 % 8;
        int r2 = step.o2 / 8, c2 = step.o2 % 8;
        sprintf(buf, "(%d,%d)-(%d,%d)", r1, c1, r2, c2);
        os << buf << " ";
    }
    os << std::endl;
}

// numbers that can only be linked by 2 lines
bool two_liner[128];
vector<int> occurrences[128];

void preprocess() {
    for (int i = 0; i < 64; ++i) {
        int color = ans_list[i];
        occurrences[color].push_back(i);
    }
    for (int color = 1; color < 128; ++color) {
        two_liner[color] = true;
        for (int i : occurrences[color]) {
            int r1 = i / 8;
            int c1 = i % 8;
            for (int j : occurrences[color]) {
                if (i == j) continue;
                int r2 = j / 8;
                int c2 = j % 8;
                if (r1 == r2 || c1 == c2)
                    two_liner[color] = false;
            }
        }
    }
}

bool try_progress(state &x) {
    bool modified = false;
    if (x.map.get_steps() >= 16)
        // we can eliminate links that are only consisted of 2 lines
    {
        for (int color = 10; color < 40; ++color) {
            if (!two_liner[color]) {
                for (int i : occurrences[color]) {
                    if (x.map.empty(i)) continue;
                    int r1 = i / 8;
                    int c1 = i % 8;
                    for (int j : occurrences[color]) {
                        if (i == j) continue;
                        int r2 = j / 8;
                        int c2 = j % 8;
                        if (x.map.empty(j)) continue;
                        if (r1 == r2 || c1 == c2)
                            goto l_exit;
                    }
                }
            }
            for (int i : occurrences[color]) {
                int r1 = i / 8;
                int c1 = i % 8;
                if (x.map.empty(i)) continue;
                for (int j : occurrences[color]) {
                    if (i == j) continue;
                    int r2 = j / 8;
                    int c2 = j % 8;
                    if (x.map.empty(j)) continue;
                    int result = x.map.search(r1, c1, r2, c2);
                    if (x.map.get_score_by_result(result) != 20) continue;
                    int score = x.map.current_score + x.map.get_score_by_result(result);

                    x.map.current_score = score;
                    x.steps.push_back(step{i, j});
                    x.map.remove(i, j);
                    modified = true;
                    break;
                }

            }
            l_exit:;

        }
    }
    return modified;
}

const int QUEUE_LIMIT = 8000;
double end_clock;

double time_in_secs() {
    timespec start{};
    clock_gettime(CLOCK_MONOTONIC, &start);
    double secs = start.tv_sec + start.tv_nsec / 1000000000.0;
    return secs;
}

void progress(unordered_map<bitset<64>, int> &cache, multiset<state, comp_state> &qu, const state &x, int factor) {
    for (int i = 0; i < 64; ++i) {
        if (x.map.empty(i)) continue;
        int r1 = i / 8;
        int c1 = i % 8;
        for (int j : occurrences[ans_list[i]])
//            for (int j = i + 1; j < 64; ++j)
        {
            if (i == j) continue;
            if (x.map.empty(j)) continue;
            int r2 = j / 8;
            int c2 = j % 8;
            int result = x.map.search(r1, c1, r2, c2);
            if (x.map.get_score_by_result(result) < 0) continue;
            int score = x.map.current_score + x.map.get_score_by_result(result);

//                    to avoid redundant computation
//                    new_s.map.link(i / 8, i % 8, j / 8, j % 8);
            auto new_s = x;
            new_s.map.remove(i, j);
            if (score > cache[new_s.map.removed]) {
                new_s.map.current_score = score;
                new_s.steps.push_back(step{i, j});
                new_s.val = comp_state{factor}.get_val(new_s);

                qu.insert(new_s);
                cache[new_s.map.removed] = score;
            }
        }
    }
}

state solve(const game_map &init_state, int factor) {
    unordered_map<bitset<64>, int> cache;
    unsigned int count_n = 0;
    multiset<state, comp_state> qu(comp_state{factor});
    qu.insert(state{init_state});
    double begin = time_in_secs();
    state best_solution;
    while (!qu.empty()) {
//        if ((count_n >> 10u) & 1u)  strange extra time cost
        if (time_in_secs() - begin > 20 || (end_clock != 0 && time_in_secs() > end_clock)) {
            cerr << "factor=" << factor << " timeout" << endl;
            break;
        }
        state x = pop_best_state(qu);
        count_n += 1;
        if (count_n % 50000 == 0) {
            cerr << "factor=" << factor << " ";
            cerr << "queue_size=" << qu.size() << " ";
            cerr << "count=" << count_n << endl;
        }
//        if (x.map.current_score == 1400) {
//            cerr << "Remaining time " << end_clock - time_in_secs() << endl;
//            exit(0);
//        }
        if (x.map.current_score > best_solution.map.current_score) {
            best_solution = x;
            show_ans(cerr, x);
            begin = time_in_secs();
        }
        if (try_progress(x))
            try_progress(x);

        progress(cache, qu, x, factor);
        while (qu.size() > QUEUE_LIMIT)
            pop_worst_state(qu);
    }
    return best_solution;
}

int main() {
    game_map map;
    ans_list = read_list(cin, 8 * 8);
    for (int i = 0; i < ans_list.size(); ++i) {
        if (ans_list[i] == 0)
            map.removed[i] = true;
    }
    preprocess();
    end_clock = time_in_secs() + 120;

    state global_best_solution;
    vector<int> factors;
    for (int factor = 30; factor > 5; factor -= 2) {
        factors.push_back(factor);
    }
    vector<state> results(factors.size());
    vector<thread> threads;
    for (int i = 0; i < factors.size(); ++i) {
        threads.emplace_back(thread([&, i]() {
            results[i] = solve(map, factors[i]);
        }));

    }
    for (int i = 0; i < factors.size(); ++i) {
        if (threads[i].joinable())
            threads[i].join();
        auto best_solution = results[i];
        if (best_solution.map.current_score > global_best_solution.map.current_score)
            global_best_solution = best_solution;
    }

    if (global_best_solution.map.get_steps() < 32) {
        cerr << "Solution not complete" << endl;
    } else {
        cerr << "Done" << endl;
    }

    show_ans(cerr, global_best_solution);
    for (auto step : global_best_solution.steps) {
        cout << step.o1 << " " << step.o2 << " ";
    }
    cout << endl;
    cout << global_best_solution.map.current_score << endl;

    return 0;
}
