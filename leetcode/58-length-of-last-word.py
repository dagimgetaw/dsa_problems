class Solution(object):
    def lengthOfLastWord(self, s):
        word_list = []

        if len(s) == 1:
            return(1)
          
        for i in range(len(s)):
            word_list.append(s[i])

  
        now = True
        rm = len(s) - 1
        while now == True:
            if s[rm] == " ":
                word_list.pop(rm)
                rm -= 1
            else:
                now = False
        value = 0

        if len(word_list) == 1:
            return(1)

        for i in range(len(word_list) - 1, -1, -1):
            if word_list[i] != " ":
                value += 1
            if word_list[i] == " ":
                break
        return(value)