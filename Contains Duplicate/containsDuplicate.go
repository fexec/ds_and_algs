func containsDuplicate(nums []int) bool {
    // Create the hashmap
    hm := make(map[int]int)
    
    for i := 0;  i < len(nums); i++ {
        // hash key will have value of one.
        hm[nums[i]]++
        // If value is found in the array again, the value will be greater than one; returning true.
        if hm[nums[i]] > 1 {
            return true
        }
    }   
    // if no value is found greater than 1, return false.
    return false
}
