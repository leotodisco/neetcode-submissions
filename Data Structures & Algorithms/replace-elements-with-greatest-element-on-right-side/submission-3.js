class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {
        let postFixes = [];
        let maxDx = -1
        for (let i = arr.length-1; i >= 0; i--) {
            if (i == arr.length-1) {
                postFixes[i] = -1;
            }
            else {
                postFixes[i] = Math.max(maxDx, arr[i+1]);
                maxDx = postFixes[i]
            }
        }

        return postFixes;
    }
}
