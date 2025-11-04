package __Two_Sum

func twoSum(nums []int, target int) []int {
	existingSum := make(map[int]int)

	for idx, num := range nums {
		diffVal := target - num
		if secondIdx, ok := existingSum[diffVal]; ok {
			return []int{secondIdx, idx}
		} else {
			existingSum[num] = idx
		}
	}
	return nil
}
