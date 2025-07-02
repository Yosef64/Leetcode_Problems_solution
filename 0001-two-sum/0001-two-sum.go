func twoSum(nums []int, target int) []int {
    dict := map[int]int{} 
    for i,v := range nums{
        t := target - v
        ind,exists := dict[t]
        if exists {
            return []int{ind,i}
        }
        dict[v] = i
    }
    return []int{}
}