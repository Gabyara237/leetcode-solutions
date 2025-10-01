class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank_num=numBottles
        empty_num=numBottles

        while empty_num >= numExchange:

            new_bottles = empty_num//numExchange #3
            empty_num= empty_num - (new_bottles*numExchange)
            drank_num += new_bottles
            empty_num += new_bottles

        return drank_num 
        