#include <bits/stdc++.h>
using namespace std;


long long countAs(string s, long long n) {
    // Return count up to n
    if (n <= s.length()) {
        unsigned long long r = 0;
        unsigned long long index = 0;
        while (n > 0) {
            r += (s[index] == 'a');
            index += 1;
            n -= 1;
        }
        return r;
    }

    // Count the number of times 'a' appears in s
    unsigned long long as = 0;
    unsigned long long mod = n % s.length();
    unsigned long long asBeforeMod = 0;
    for(long long i = 0; i < s.length(); i++) {
        if (s[i] == 'a') {
            as += 1;
            asBeforeMod += i < mod ? 1 : 0;
        }
    }

    // If n equals the length of the string, return the count so far
    if (mod == 0) {
        return as * (n / s.length());
    } else {
        // unsigned long long offset = 0;
        return as * (n / s.length()) + asBeforeMod;
    }
}


int main() {
    string s; getline(cin, s);
    long long n; cin >> n;

    long long r = countAs(s, n);

    cout << r << endl;
    return 0;
}
