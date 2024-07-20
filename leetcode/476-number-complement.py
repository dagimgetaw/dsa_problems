class Solution:
    def findComplement(self, num: int) -> int:
        from math import floor, pow
        
        r = True
        array = []
        new_array = []

        if num == 1:
            return 0

        while r:
            if num % 2 == 0:
                num = num / 2
                array.append(0)
            else:
                num = floor(num / 2)
                array.append(1)

            if num == 0:
                array.append(0)
                r = False
            if num == 1:
                array.append(1)
                r = False

        array.reverse()

        length = len(array)
        index = 0

        while length != 0:
            if array[index] == 0:
                new_array.append(1)
            else:
                new_array.append(0)
            index += 1
            length -= 1

        new_array.reverse()

        total = 0
        power = 0

        for i in new_array:
            total += pow((i * 2), power)
            power += 1

        if new_array[0] == 0:
            total = total - 1

        total = int(total)

        return total