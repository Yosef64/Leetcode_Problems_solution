class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year , month , date = date.split("-")
        return f"{bin(int(year))[2:]}-{bin(int(month))[2:]}-{bin(int(date))[2:]}"
        