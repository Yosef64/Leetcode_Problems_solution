func kthCharacter(k int) byte {
    ans := "a"
    for len(ans) < k{
        ans += GenerateNextString(ans)
    }
    fmt.Print(ans)
    return ans[k-1]
}

func GenerateNextString(s string) string{
    res := ""
    for _,char := range s{
        ascii := int(char) - 97
        next_char := (ascii + 1) % 26 + 97
        res += string(rune(next_char))
    }
    return res
}