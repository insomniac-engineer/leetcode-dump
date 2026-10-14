class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        #1 1
        #2 3 x + 1 y + 1
        #3 4 x + 1 y + 1

        # 2 3
        # 1 2
        # 0 1
        # -1 0


        res = 0
        x = points[0][0]
        y = points[0][1]
        for p in points:

            while x != p[0] or y!= p[1]:
                # print("x = ", x)
                # print("x needed = ", p[0])
                # print("y = ", y)
                # print("y needed = ", p[1])
                res += 1
                if x < p[0]:
                    x += 1
                elif x > p[0]:
                    x -= 1
                if y < p[1]:
                    y += 1
                elif y > p[1]:
                    y -= 1
                # print("---")
                # print("x = ", x)
                # print("x needed = ", p[0])
                # print("y = ", y)
                # print("y needed = ", p[1])
        return res