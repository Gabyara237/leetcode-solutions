class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution O(n) - Find the longest substring without duplicate characters
        # Using the sliding window technique with two pointer (left, right) 
        # Dictionary store each character and its most recente index
        # When duplicate found, move left pointer to the index of the previous occurrence plus 1

        last_seen={}
        left = 0
        result = 0

        for i, character in enumerate(s):
            if character in last_seen and last_seen[character]>= left:
                left = last_seen[character] +1
            
            last_seen[character] = i
            result = max(result, i-left+1)
        
        return result





        