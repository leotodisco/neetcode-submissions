class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let maxCons = 0;
        let streak = 0;

        for (let i = 0; i < nums.length; i++){
            if (nums[i] == 1) {
                streak+=1;
                maxCons = Math.max(streak, maxCons);
            }
            else {
                streak = 0;
            }
        }

        return maxCons;
    }   
}
