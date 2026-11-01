class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsSet = new Set();

        for (const n of nums) {
            if (numsSet.has(n)) {
                return true;
            }
            numsSet.add(n);
        }

        return false;
    }
}
