class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # cool version
        n = 0
        for number in A:
            n = n ^ number
        
        return n


# ## for testing
def main():
    testPoints = [0, 1, 0, 3, 2, 5, 2, 3, 1]
    sol = Solution()
    result = sol.singleNumber(testPoints)

    print 'Result: ' + str(result)


if __name__ == "__main__":
    main()