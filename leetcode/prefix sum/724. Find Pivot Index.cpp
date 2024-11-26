class Solution {
public:
    int pivotIndex(vector<int>& nums) {

        int n = nums.size();
        int total, leftsum = 0;

        for (int num : nums) {
            total += num;
        }

        for (int i = 0; i < n; i++) {
            int rightsum = total - leftsum - nums[i];

            if (leftsum == rightsum) {
                return i;
            }

            leftsum += nums[i];
        }
    
        return -1;

    }
};