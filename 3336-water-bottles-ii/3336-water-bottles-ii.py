class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        new_bottles=0
        empty_bottles= numBottles
        drunk_bottles= empty_bottles

        while empty_bottles>= numExchange:
            # Exchange bottles
            new_bottles=1
            empty_bottles-=numExchange

            # Drink new bottles
            drunk_bottles+=new_bottles
            empty_bottles+=1
            numExchange+=1 
        
        return drunk_bottles

