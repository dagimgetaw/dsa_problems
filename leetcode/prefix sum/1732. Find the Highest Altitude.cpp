class Solution {
public:
    int largestAltitude(vector<int>& gain) {

        int n = gain.size();
        int arr[n + 1];

        arr[0] = 0;

        for (int i = 0; i < n; i++) {
            int m = i + 1;
            arr[m] = arr[m - 1] + gain[i]; 
        }

        int high = arr[0];

        for (int num : arr) {
            if (num > high) {
                high = num;
            }
        } 

        return high;
        
    }
};