#include <bits/stdc++.h>
using namespace std;

int main(){
    // Counter, temporary n and maximum value
    int c, n, max = 0;

    // Ignore N
    cin.ignore();

    while(cin >> n)
        n > max ? c = !!(max = n) : c += (n == max);

    // Print counter
    cout << c << "\n";

    return 0;
}
