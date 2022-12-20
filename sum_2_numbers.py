class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if num1 is None:
            return num2
        if num2 is None:
            return num1
            return
        _sum = int(num1 + num2)
        return _sum

if __name__=="__main__":
    sol = Solution()
    print(sol.sum(-1, 10))
    """
    Time complexity: 0(1)
    Space complexity: 0(1)
    """

