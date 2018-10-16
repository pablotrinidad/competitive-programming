#include <bits/stdc++.h>
using namespace std;

int diamonds(string s, int i, int o, int c) {
    if (i >= s.length()) { return 0; }

    if (s[i] == '<') { o = i; }
    else if (s[i] == '>' && o != -1) { c = i; }

    if (o != -1 && c != -1) {
        s = s.substr(0, o) + s.substr(c + 1, s.length() - 1);
        return 1 + diamonds(s, 0, -1, -1);
    } else {
        return diamonds(s, i + 1, o, c);
    }
}

int main() {
    string s;
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; ++i) {
        getline (cin, s);
        cout << diamonds(s, 0, -1, -1) << endl;
    }
    return 0;
}
