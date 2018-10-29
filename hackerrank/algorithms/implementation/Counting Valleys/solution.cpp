#include <bits/stdc++.h>
using namespace std;

int countValleys(int n, string s) {
    int level = 0, valleys = 0;
    int step;
    for(int i=0; i<s.length(); i++) {
        step = s[i] == 'D' ? -1 : 1;
        if (level < 0 && level + step == 0)
            valleys ++;
        level += step;
    }
    return valleys;
}

int main() {
    int n; cin >> n;
    string s; cin >> s;

    int valleys = countValleys(n, s);

    cout << valleys << endl;

    return 0;
}
