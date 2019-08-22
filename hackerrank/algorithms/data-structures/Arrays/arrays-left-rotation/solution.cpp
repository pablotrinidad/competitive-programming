#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    int d; cin >> d;
    int l[n];
    for(int i = 0; i < n; i++) {
        i - d < 0 ? cin >> l[n - d + i] : cin >> l[i - d];
    }

    for(int i = 0; i < n; i++) { cout << l[i]<< " "; }
    cout << endl;
    return 0;
}
