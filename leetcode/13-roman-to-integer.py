class Solution(object):
    def romanToInt(self, s):
        value  = 0
        over = 0

        target_number = []
        for i in s:
            target_number.append(i)
        length = len(target_number)
        target_number.insert(length, " ")
        for i in range(0, length):
            if target_number[i] == 'I' and target_number[i + 1] == 'V':
                    value += 4
                    over += 5
            elif target_number[i] == 'I'and target_number[i + 1] == 'X':
                    value += 9
                    over += 10
            elif target_number[i] == 'I':
                    value += 1
            elif target_number[i] == 'V':
                value += 5
            elif target_number[i] == 'X' and target_number[i + 1] == 'L':
                    value += 40
                    over += 50
            elif target_number[i] == 'X' and target_number[i + 1] == 'C':
                    value += 90
                    over += 100
            elif target_number[i] == 'X':
                    value += 10
            elif target_number[i] == 'L':
                value += 50
            elif target_number[i] == 'C' and target_number[i + 1] == 'D':
                    value += 400
                    over += 500
            elif target_number[i] == 'C' and target_number[i + 1] == 'M':
                    value += 900
                    over += 1000
            elif  target_number[i] == 'C':
                    value += 100
            elif target_number[i] == 'D':
                value += 500
            elif target_number[i] == 'M':
                value += 1000
            else:
                value += 0
        return(value-over)
        
