class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        num, flag = (num, '') if num >= 0 else (abs(num), '-')
        while True:
            q, r = divmod(num, 7)
            result.append(r)
            if num < 7:
                break
            num = q
        return flag + ''.join(map(str, reversed(result)))
