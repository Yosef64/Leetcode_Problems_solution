func searchMatrix(matrix [][]int, target int) bool {
    for _,val:= range matrix{
        if isExist:= BinarySearch(val,target); isExist{
            return true
        }
    }
    return false
    
}
func BinarySearch(row []int,tar int) bool{
    l , r := 0,  len(row) - 1
    for l <= r{
        mid := (r+l)/2
        if row[mid] == tar {
            return true
        }
        if row[mid] > tar{
            r = mid - 1
        }else{
            l = mid + 1
        }

    }
    return false
}