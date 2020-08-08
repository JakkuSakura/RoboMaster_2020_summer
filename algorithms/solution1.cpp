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
};


struct comp_state {
    int factor;

    int get_val(int current_score, int steps) {
        return current_score - steps * factor;
    }

    int get_val(const state &s) {
        return get_val(s.map.current_score, s.map.get_steps());
    }

    bool operator()(const state &lhs, const state &rhs) {
        return get_val(lhs) > get_val(rhs);
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

state get_worst_state(multiset<state, comp_state> &qu) {
    auto it = --qu.end();
    return *it;
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

const int QUEUE_LIMIT = 100000;

state solve(const game_map &init_state, int factor) {
    unordered_map<bitset<64>, int> cache;
    int count_n = 0;
    multiset<state, comp_state> qu(comp_state{factor});
    qu.insert(state{init_state});
    clock_t begin = clock();
    state best_solution;
    while (!qu.empty()) {
        if (double(clock() - begin) / CLOCKS_PER_SEC > 45) {
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
        if (x.map.current_score > best_solution.map.current_score) {
            best_solution = x;
            show_ans(cerr, x);
            begin = clock();
        }

        for (int i = 0; i < 64; ++i) {
            int r1 = i / 8;
            int c1 = i % 8;
            if (x.map.empty(r1, c1)) continue;
            for (int j = i + 1; j < 64; ++j) {
                int r2 = j / 8;
                int c2 = j % 8;
                if (x.map.empty(r2, c2)) continue;
                int result = x.map.search(r1, c1, r2, c2);
                if (x.map.get_score_by_result(result) < 0) continue;
                int score = x.map.current_score + x.map.get_score_by_result(result);

//                    to avoid redundant computation
//                    new_s.map.link(i / 8, i % 8, j / 8, j % 8);
                auto new_s = x;
                new_s.map.current_score = score;
                new_s.steps.push_back(step{i, j});
                new_s.map.remove(r1, c1, r2, c2);
                if (score > cache[new_s.map.removed]) {
                    qu.insert(new_s);
                    cache[new_s.map.removed] = score;
                }
            }
        }
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
    cout << std::endl;

}
