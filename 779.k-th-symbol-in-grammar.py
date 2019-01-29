class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if K == 1:
            return 0

        nth, decrease = self.get_nth(K)
        k = 2 ** (nth - 1) - decrease
        return 1 - self.kthGrammar(N, k)

    def get_nth(self, num):
        nth = 0
        while True:
            if 2 ** nth >= num:
                break
            nth += 1
        return nth, 2 ** nth - num
