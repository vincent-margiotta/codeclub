from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_and_stones = Counter(stones)
        return sum(jewels_and_stones[k] for k in jewels)

if __name__ == '__main__':
    test = Solution()
    result = test.numJewelsInStones("aA", "aAAbbbb")
    print(result)