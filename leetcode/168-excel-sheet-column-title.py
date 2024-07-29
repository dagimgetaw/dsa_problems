class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        column_title = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            column_title = chr(65 + remainder) + column_title
            columnNumber = columnNumber // 26

        return column_title