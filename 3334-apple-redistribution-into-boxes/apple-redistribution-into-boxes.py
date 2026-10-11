class Solution(object):

    def minimumBoxes(self, apple, capacity):

        total_apples = sum(apple)
        capacity.sort(reverse=True)
        total_capacity = 0
        boxes = 0

        for c in capacity:
            total_capacity += c
            boxes += 1

            if total_capacity >= total_apples:
                return boxes