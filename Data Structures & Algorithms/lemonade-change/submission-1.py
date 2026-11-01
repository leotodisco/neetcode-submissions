class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0

        for n in bills:
            if n == 5:
                count5 += 1

            elif n == 10:
                if count5 == 0:
                    return False
                count10+=1
                count5-=1
                
            elif n == 20:
                if count10 > 0 and count5 > 0:
                    count10-=1
                    count5-=1
                elif count5 >= 3:
                    count5-=3
                else:
                    return False
            
        
        return True
                

        