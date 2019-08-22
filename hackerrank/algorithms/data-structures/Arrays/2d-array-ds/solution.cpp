#include <bits/stdc++.h>
using namespace std;


int getMaxHourglass(int arr[6][6]) {
    int r = numeric_limits<int>::min();
    for(int row = 0; row < 4; row++) {
        for(int col = 0; col < 4; col++) {
            int s = (
                arr[row][col] + arr[row][col+1] + arr[row][col+2] +
                arr[row+1][col+1] +
                arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            );
            r = max(r, s);
        }
    }
    return r;
}


int main() {
    int arr[6][6];
    for(int i = 0; i < 6; i++) {
        for(int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }
    }

    int r = getMaxHourglass(arr);

    cout << r << endl;

    return 0;
}
