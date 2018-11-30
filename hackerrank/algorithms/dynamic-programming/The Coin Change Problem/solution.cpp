#include <bits/stdc++.h>
using namespace std;


int main() {
    int n; int k;
    cin >> n; cin >> k;
    int coins[k];
    for (int i = 0; i < k; ++i)
        cin >> coins[i];

    long dp[n + 1];
    fill(dp, dp+n+1, 0);
    dp[0] = 1;

    for (int i = 0; i < k; i++) {
        for(int j = 0; j <= n; j++) {
            int r = j - coins[i];
            dp[j] += r < 0 ? 0 : dp[r];
        }
    }

    cout << dp[n] << endl;

    return 0;
}
