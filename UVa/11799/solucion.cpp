#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a, c, max=0;
    cin.ignore(); cin.ignore(); // Ignore number of test cases
    while (cin >> n) { // Ignore number of students
        c += 1;
        for (int i = 0; i < n; ++i) {
            cin >> a;
            a > max ? max = a : max = max;
        }
        cout << "Case " << c << ": " << max << "\n";
        max = 0;
    }
    return 0;
}
