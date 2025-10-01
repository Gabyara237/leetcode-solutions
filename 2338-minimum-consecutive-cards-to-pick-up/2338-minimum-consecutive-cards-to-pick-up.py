class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        result= float('inf')

        for i, num in enumerate(cards):
            if num in dic:
                result= min(result, i- dic[num]+1)
            dic[num]=i  
        
        return result if result != float('inf') else -1

            