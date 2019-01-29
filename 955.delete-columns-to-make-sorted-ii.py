class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A or not A[0]:
            return 0

        D = set()
        s_length = len(A[0])
        i = 0

        while True:
            if len(D) == s_length or i == len(A) - 1:
                return len(D)

            s = A[i]
            next_s = A[i+1]
            # compare
            for s_i in range(s_length):
                if s_i in D:
                    continue
                if s[s_i] > next_s[s_i]:
                    i = -1
                    D.add(s_i)
                elif s[s_i] < next_s[s_i]:
                    break
            i += 1
