func smallestDivisor(nums []int, threshold int) int {
    sort.Ints(nums)
    _,max:= sumAndMax(nums)
    ans := math.MaxInt64
    low,high := 1,max
    for low <= high{
        mid := (high - low) / 2 + low
        if SumWithDivision(nums,mid) <= threshold{
            high = mid - 1
            ans = mid
        }else{
            low = mid + 1
        }
    }
    return ans


}

func sumAndMax(arr []int)(int,int){
 res := 0
 max := 0
 for _,v:= range arr{
    res += v
    max = int(math.Max(float64(max),float64(v)))
 }
 return res,max
}
func SumWithDivision(arr []int,divisor int) int {
    sum := 0
    for _,val := range arr{
        sum += int(math.Ceil(float64(val)/float64(divisor)))
    }
    return sum
}