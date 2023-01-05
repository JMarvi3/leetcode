class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        places = {v: i+1 for i, v in enumerate(sorted(score, reverse=True))}
        result = []
        for num in score:
            place = places[num]
            result.append(ranks.get(place, str(place)))
        return result