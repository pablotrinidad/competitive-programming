#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    int pairs[100];
    int count = 0;

    for (int i = 0; i < n; ++i) {
        int c; cin >> c;
        pairs[c-1] == c ? pairs[c-1] = !(count+=1) : pairs[c-1] = c;
    }

    cout << count << "\n";

    return 0;
}
