class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let ans = [];
        for (let i = 0; i < (2*nums.length); i++) {
            ans[i] = nums[i % nums.length];
        }

        return ans
    }
}
