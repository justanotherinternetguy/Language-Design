// UNFINISHED AND REALLY DUMB IMPLEMENTATION OF BRAINF*** WITHOUT ANY GOING BACK :)
/* 
 * PRINT "HI"
 * up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-down-out-next-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-up-down-out
*/

#include <bits/stdc++.h>

using namespace std;

void pincr(int ptr) {
    ++ptr;
}

void bincr(int data[], int ptr) {
    ++data[ptr];
}

void puts(int data[], int ptr) {
    cout << (char) (data[ptr] + 32);
}

void gets(int data[], int ptr) {
    cin >> data[ptr];
}


void run(vector<string> code) {
    int MAX = 1000;
    int data[MAX];
    int ptr = 0;

    for (auto tk : code) {
        if (data[ptr] <= 18) {
            if (tk == "up") { bincr(data, ptr); }
        }

        if (data[ptr] > 18) {
            if (tk == "down") { bincr(data, ptr); }
        }

        if (tk == "next") { pincr(ptr); }
        if (tk == "out") { puts(data, ptr); }
    }
}


int main() {
    vector<string> code;
    string s, temp;
    cin >> s;
    stringstream ss(s);

    while (getline(ss, temp, '-')) {
        code.push_back(temp);
    }

    run(code);
}
