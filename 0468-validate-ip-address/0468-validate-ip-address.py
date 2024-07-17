class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def Ipv6(arr):
            if len(arr) != 8:return False

            for word in arr:
                n = len(word)
                if n > 4 or n == 0:return False

                for char in word:
                    if char.isalpha() and not 96 <= ord(char.lower()) <103:
                        return False
            return True
        def Ipv4(arr):
            if len(arr) != 4:return False

            for word in arr:
                if (len(word) > 1 and word[0] == '0') or not word.isnumeric() or int(word) > 255:
                    return False
            return True
        
        first = Ipv6(queryIP.split(':'))
        second = Ipv4(queryIP.split('.'))
        if first:return "IPv6"
        elif second:return "IPv4"
        return "Neither"
