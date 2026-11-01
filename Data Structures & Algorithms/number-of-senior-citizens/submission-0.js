class Solution {
    /**
     * @param {string[]} details
     * @return {number}
     */
    countSeniors(details) {
        let totalSeniors = 0;
        for (let i = 0; i < details.length; i++) {
            const age = details[i].slice(11, 13);
            if (Number(age) > 60) {
                totalSeniors+=1;
            }
            
        }

        return totalSeniors;
    }
}
