#include <bits/stdc++.h>
using namespace std;

int diamonds(string s) {
    int o = 0; int d = 0;
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == '<') { o += 1; }
        else if (s[i] == '>' && o > 0) { d += 1; o -= 1; }
    }
    return d;
}

int main() {
    string s;
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; ++i) {
        getline (cin, s);
        cout << diamonds(s) << endl;
    }
    return 0;
}
