#include <bits/stdc++.h>
using namespace std;

int getMinJumps(int n, int clouds[]) {
    int jumps = 0;
    n -= 1;
    while (n > 0) {
       clouds[n - 2] == 1 ? n -= 1 : n -= 2;
       jumps += 1;
    }
    return jumps;
}

int main() {
    int n; cin >> n;
    int clouds[n];
    for (int i = 0; i < n; ++i)
        cin >> clouds[i];

    int jumps = getMinJumps(n, clouds);

    cout << jumps << endl;

    return 0;
}
