from collections import defaultdict
import numpy as np

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # first sort the array by the x-index
        points = sorted(points, key=lambda x: (x[0],-x[1]))
        
        # maintain an array of the structure of a max-y <-> min-y structure
        y_points_dict = defaultdict(list)
        for i in range(len(points)):
            # the points are now (i, points[i]), e.g. (0, [1,1])
            x = points[i][0]
            y = points[i][1]
            y_points_dict[y].append([i, points[i]])

        sorted_y_points = dict(sorted(y_points_dict.items()))

        y_stack = []
        for item in sorted_y_points.items():
            point_list = item[1][::-1]
            for point in point_list:
                y_stack.append(point[0])

        # for the y_stack, for any new node on the right side, it will construct a pair with any node which is on the left side of it and has a smaller index. At the same time, there cannot be any in-between index between them.
        y_stack = y_stack[::-1]
        print(y_stack)
        cnt = 0
        for i in range(1, len(y_stack)):
            min_value = -10000000000
            current_value = y_stack[i]
            #print("the current i:", i)
            for j in range(i-1, -1, -1):
                #print("the current j:", j)
                if y_stack[j] < current_value and y_stack[j] > min_value:
                    cnt += 1
                    min_value = y_stack[j]
                    #print("j matches the pair")
                #else:
                    #print("j doesn't match the pair")

        return cnt
