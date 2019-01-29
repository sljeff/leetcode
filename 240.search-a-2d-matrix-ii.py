class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        max_x, max_y = (len(matrix[0]) - 1), (len(matrix) - 1)
        x, y = max_x, 0
        while True:
            value = matrix[y][x]
            if target == value:
                return True
            if target < value:
                x -= 1
                if x < 0:
                    return False
            else:
                y += 1
                if y > max_y:
                    return False
