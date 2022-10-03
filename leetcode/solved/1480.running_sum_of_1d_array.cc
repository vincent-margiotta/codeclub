class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sum (nums.size());
        int running = 0;

        for(int i = 0; i < nums.size(); i++) {
            running += nums[i];
            sum[i] = running;
        }
        return sum;
    }
};
