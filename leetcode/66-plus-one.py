class Solution(object):
    def plusOne(self, digits):

        single_int = int(''.join(map(str, digits)))
        single_int += 1
        single_int = str(single_int)
        int_list = []

        for i in single_int:
            i = int(i)
            int_list.append(i)

        return(int_list)
        