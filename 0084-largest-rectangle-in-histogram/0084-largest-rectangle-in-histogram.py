class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Add a sentinel value to flush out remaining bars in stack

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                print(i,heights[i])
                if stack:
                    print(stack[-1], i - stack[-1] - 1, i - stack[-1] )
                print('-----')
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area


        

        