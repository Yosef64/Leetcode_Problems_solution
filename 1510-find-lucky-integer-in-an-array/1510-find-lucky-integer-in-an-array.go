func findLucky(arr []int) int {
    ans := -1.0
    freq := GetFrequency(arr)
    for key,val := range freq{
        if key == val{
            ans = math.Max(float64(key),ans)
        }
    }
    return int(ans)
}
func GetFrequency(arr []int) map[int]int{
    dict := make(map[int]int)
    for _,val := range arr{
        dict[val] += 1
    }
    return dict
}