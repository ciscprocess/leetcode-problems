__author__ = 'Nathan'

class Solution:

    def calcBestPath(self, vec):
        pass

    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        x, y = 0, 0
        startPenalty = dungeon[y][x]
        delta = -999999999

        m = len(dungeon)
        n = len(dungeon[0])

        for i in range(m + n):
            pass

        return max(-delta + 1, 1)




# for testing
def main():
    testGrid = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]

    sol = Solution()
    result = sol.calculateMinimumHP(testGrid)

    print 'Result: ' + str(result)


if __name__ == "__main__":
    main()