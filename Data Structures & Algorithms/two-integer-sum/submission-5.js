class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashMap = {}

        for (let i = 0; i < nums.length; i++) {
            const diff = target - nums[i]
            if (diff in hashMap){
                return new Array(hashMap[diff], i);
            }
            else {
                hashMap[nums[i]] = i;
            }

        }

        return new Array();
    }
}
