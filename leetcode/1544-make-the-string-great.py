class Solution:
    def makeGood(self, s: str, prev_res: str = "") -> str:
        # handle base case first
        if len(s) < 2:
            return prev_res + s

        # split important values out for convenience
        current = s[0]
        next = s[1]
        is_same_char = current.lower() == next.lower()
        not_same_case = current.isupper() != next.isupper()

        # natural recursion
        if is_same_char and not_same_case:
            if prev_res == "":
                return self.makeGood(
                    s[2:],
                    prev_res
                )
            return self.makeGood(
                prev_res[-1] + s[2:],
                prev_res[:-1]
            )
        else:
            return self.makeGood(
                s[1:],
                prev_res + current
            )
