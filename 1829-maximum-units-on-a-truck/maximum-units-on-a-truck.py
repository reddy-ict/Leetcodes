class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total = 0

        for boxes, units in boxTypes:
            if truckSize >= boxes:
                total += boxes * units
                truckSize -= boxes
            else:
                total += truckSize * units
                break

        return total