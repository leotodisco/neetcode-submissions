class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    scoreOfString(s) {
        const lenS = s.length;
        let tot = 0;

        for (let i = 1; i < lenS; i++) {
            
            tot+=Math.abs(s[i].charCodeAt(0) - s[i-1].charCodeAt());
        }

        return tot;
    }
}
