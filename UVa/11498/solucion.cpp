#include <bits/stdc++.h>
using namespace std;

int main () {
    int k, n, m, x, y;
    string l;
    while (cin >> k && k != 0) {
        cin >> n >> m;
        for (int i = 0; i < k; ++i) {
            cin >> x >> y;
            x = x - n;
            y = y - m;
            if (x == 0 || y == 0)
                cout << "divisa" << endl;
            else {
                y > 0 ? l+= 'N' : l+= 'S';
                x > 0 ? l+= 'E' : l+= 'O';
                cout << l << endl;
            }
            l = "";
        }
    }
    return 0;
}
