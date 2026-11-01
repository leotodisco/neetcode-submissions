class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums, k) {
        let hashset = new Set();
        for(let i = 0; i < nums.length; i++) {
            if (hashset.has(nums[i])) {
                return true;
            }

            hashset.add(nums[i])

            if (hashset.size > k) {
                hashset.delete(nums[i-k])
            }

        }

        return false;
    }
}
