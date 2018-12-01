#include <bits/stdc++.h>
using namespace std;

int sherlock(int b[], int n) {
    int paths[2] = {b[0], 1};
    int r[2] = {0};
    for(int i = 1; i < n; i++) {
        for(int j = 0; j < 2; j++) {
            int withB = abs(paths[j] - b[i]);
            int withoutB = paths[j] - 1;
            withB > withoutB ? paths[j] = b[i] : paths[j] = 1;
            r[j] += max(withB, withoutB);
        }
    }
    return max(r[0], r[1]);
}

int main() {
    int t; cin >> t;
    while (t > 0) {
        int n; cin >> n;
        int b[n];
        for (int i = 0; i < n; i++) { cin >> b[i]; }
        cout << sherlock(b, n) << endl;
        t -= 1;
    }

    return 0;
}
