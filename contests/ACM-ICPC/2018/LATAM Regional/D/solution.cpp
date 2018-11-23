#include <bits/stdc++.h>
using namespace std;

int countUniques(vector <string> emails) {
    unordered_set <string> uniques;

    for(int i = 0; i < emails.size(); i++) {
        string tag = "";
        bool valid = true;
        for(int j = 0; j < emails[i].length(); j++) {
            char c = emails[i][j];
            if(c == '@') {
                tag += emails[i].substr(j, emails[i].length() - j);
                break;
            } else if (c == '+') {
                valid = false;
            } else if(c != '.' and valid) {
                tag += c;
            }
        }

        if(uniques.count(tag) == 0) {
            uniques.insert(tag);
        }
    }
    return uniques.size();
}

int main() {
    int n; cin >> n;
    vector <string> emails;

    for(int i = 0; i < n; i++) {
        string email; cin >> email;
        emails.push_back(email);
    }

    int c = countUniques(emails);
    cout << c << "\n";

    return 0;

}
