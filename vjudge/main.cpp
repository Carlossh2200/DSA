#include <iostream>
#include <vector>

using namespace std;

int binarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<int> array(N);

    for (int i = 0; i < N; i++) {
        cin >> array[i];
    }

    for (int i = 0; i < Q; i++) {
        int query;
        cin >> query;
        int position = binarySearch(array, query);
        cout << position << endl;
    }

    return 0;
}
