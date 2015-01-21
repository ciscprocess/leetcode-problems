# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        dict_count = dict()
        count = 0
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points[i + 1:]):
                count += 1
                slope = float((point2.y - point1.y))

                b = 0

                if (point2.x - point1.x) == 0:
                    slope = float('inf')
                    b = point1.x
                else:
                    slope /= float((point2.x - point1.x))
                    b = point1.y - slope * point1.x

                slope = round(slope, 8)
                b = round(b, 8)

                if not (slope, b) in dict_count:
                    dict_count[(slope, b)] = [0] * len(points)

                dict_count[(slope, b)][i] = 1
                dict_count[(slope, b)][j + i + 1] = 1

        max_size = 0 if len(points) == 0 else 1

        print 'Count: ' + str(count) + '/' + str(len(points))

        for k in dict_count:
            max_size = max(max_size, sum(dict_count[k]))

        return max_size


# ## for testing
def main():
    testPoints = [Point(560,248),Point(0,16),Point(30,250),Point(950,187),Point(630,277),Point(950,187),Point(-212,-268),Point(-287,-222),Point(53,37),Point(-280,-100),Point(-1,-14),Point(-5,4),Point(-35,-387),Point(-95,11),Point(-70,-13),Point(-700,-274),Point(-95,11),Point(-2,-33),Point(3,62),Point(-4,-47),Point(106,98),Point(-7,-65),Point(-8,-71),Point(-8,-147),Point(5,5),Point(-5,-90),Point(-420,-158),Point(-420,-158),Point(-350,-129),Point(-475,-53),Point(-4,-47),Point(-380,-37),Point(0,-24),Point(35,299),Point(-8,-71),Point(-2,-6),Point(8,25),Point(6,13),Point(-106,-146),Point(53,37),Point(-7,-128),Point(-5,-1),Point(-318,-390),Point(-15,-191),Point(-665,-85),Point(318,342),Point(7,138),Point(-570,-69),Point(-9,-4),Point(0,-9),Point(1,-7),Point(-51,23),Point(4,1),Point(-7,5),Point(-280,-100),Point(700,306),Point(0,-23),Point(-7,-4),Point(-246,-184),Point(350,161),Point(-424,-512),Point(35,299),Point(0,-24),Point(-140,-42),Point(-760,-101),Point(-9,-9),Point(140,74),Point(-285,-21),Point(-350,-129),Point(-6,9),Point(-630,-245),Point(700,306),Point(1,-17),Point(0,16),Point(-70,-13),Point(1,24),Point(-328,-260),Point(-34,26),Point(7,-5),Point(-371,-451),Point(-570,-69),Point(0,27),Point(-7,-65),Point(-9,-166),Point(-475,-53),Point(-68,20),Point(210,103),Point(700,306),Point(7,-6),Point(-3,-52),Point(-106,-146),Point(560,248),Point(10,6),Point(6,119),Point(0,2),Point(-41,6),Point(7,19),Point(30,250)]
    sol = Solution()
    result = sol.maxPoints(testPoints)

    print 'Result: ' + str(result)


if __name__ == "__main__":
    main()