class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        queue = list(s)
        for _ in range(len(queue)):
            current = queue.pop(0)

            if res and current.lower() == res[-1].lower() and current.isupper() != res[-1].isupper():
                res.pop()
            else:
                res.append(current)

        return ''.join(res)
