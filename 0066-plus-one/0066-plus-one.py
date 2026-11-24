class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = [1]
        for i in range(-1,-len(digits)-1,-1):
            if digits[i]==9:
                digits[i]=0
                if digits[0]==0:
                    d.extend(digits)
                    return d
                
            else:
                digits[i] += 1
                break
        
        return digits







        