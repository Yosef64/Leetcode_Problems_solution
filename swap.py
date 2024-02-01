def swap_case(s):
    ans = ""
    for char in s:
        if char.islower():
            ans+=char.upper()
        else:
            ans+=char.lower()
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
