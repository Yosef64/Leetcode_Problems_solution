func maxDistance(position []int, m int) int {
    sort.Ints(position)
    left := 1
    right := position[len(position)-1]/(m-1) + 1
    ans := 0
    for left <= right{
        mid := (right - left)/2 + left
        if canPlace(mid,position,m){
            ans = mid
            left = mid + 1
        } else{
            right = mid - 1
        }
        
    }
    return ans

}


func canPlace(d int,position []int,m int) bool{
    last_pos := position[0]
    last_ball := 1
    for i := 1;i < len(position);i++{
        if gap := position[i] - last_pos;gap >= d{
            last_ball += 1
            last_pos = position[i]
        }
        if last_ball == m{
            return true
        }
    }
    return false
    
}