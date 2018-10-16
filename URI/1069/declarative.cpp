#include <bits/stdc++.h>
using namespace std;

int diamonds(string s) {
    int o = -1, c = -1;
    int d = 0, i = 0;
    while (i < s.length() && s.length() > 1) {
        if (s[i] == '<') { o = i; }
        else if (s[i] == '>' && o != -1) { c = i; }

        if (c != -1 && o != -1) {
            s = s.substr(0, o) + s.substr(c + 1, s.length() - 1);
            d += 1; i = 0;
            o = -1; c = -1;
        } else {
            i += 1;
        }
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
