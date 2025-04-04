class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1: return ceil(piles[0] / h)
        sorted_piles = sorted(piles)
        min, max = self.check_hrs(h, sorted_piles, sorted_piles)
        return self.check_hrs(
            h,
            sorted_piles,
            range(min if min is not max else 1, max + 1)
        )[1]

    def check_hrs(
        self,
        h: int,
        piles: List[int],
        k_candidates: type[List[int] | range]
    ) -> (int, int):
        min_idx = 0
        max_idx = len(k_candidates)

        curr_idx = ceil((max_idx - min_idx) / 2)
        while min_idx < max_idx:
            k = k_candidates[curr_idx]
            hours_used = h
            for pile in piles:
                hours_used -= ceil(pile / k)
            if hours_used < 0:
                min_idx = curr_idx + 1
                curr_idx += ceil((max_idx - min_idx) / 2)
                continue
            max_idx = curr_idx
            curr_idx -= ceil((max_idx - min_idx) / 2)
        return (k_candidates[max(max_idx, 0)], k_candidates[min(min_idx, len(k_candidates) - 1)])
