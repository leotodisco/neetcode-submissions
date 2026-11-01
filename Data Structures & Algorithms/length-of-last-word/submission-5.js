class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLastWord(s) {
        s = s.trim();
        let tot = 0;
        for (let i = s.length-1; i >= 0; i--) {
            if (s[i] === " ") {
                return tot;
            }
            tot+=1;
        }


        return tot;
    }
}
