class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        s = ""
        k = 0
        
        while l < len(chars):
            r = 0
            groupLen = 0
            
            while l+r < len(chars) and chars[l]==chars[l+r]:
                groupLen += 1
                r+=1

            if groupLen > 1:
                s += f"{chars[l]}{groupLen}"
                k += len(f"{chars[l]}{groupLen}")
            else:
                s += f"{chars[l]}"
                k += 1
            l+=r
        

        for index, c in enumerate(s):
            chars[index] = c
        return k
            
                
            
