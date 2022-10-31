class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int jewels_count = 0;
        for(int i=0; i<stones.length(); i++) {
            if (jewels.find(stones[i]) != string::npos) {
                jewels_count += 1;
            }
        }
        return jewels_count;
    }
};