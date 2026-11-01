class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        indexW = 0
        indexA = 0

        while indexW < len(word) and indexA < len(abbr):
            if abbr[indexA] == '0':
                return False

            if word[indexW] == abbr[indexA]:
                indexW+=1
                indexA+=1
            
            elif abbr[indexA].isalpha():
                return False        
            
            else:
                subStr = ""
                while indexA < len(abbr) and abbr[indexA].isdigit():
                    subStr+=abbr[indexA]
                    indexA+=1
                indexW += int(subStr)
                    
        return indexW == len(word) and indexA == len(abbr)

