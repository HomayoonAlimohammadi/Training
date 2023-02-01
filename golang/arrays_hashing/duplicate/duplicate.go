package duplicate

import (
	"fmt"
	"time"
)

func ContainsDuplicate() {
	t0 := time.Now()
	fmt.Println("Running Contains Duplicate...")

	nums := []int{1, 2, 3, 1}
	fmt.Printf("\nInput: %v \n", nums)
	ans := containsDuplicate(nums)
	fmt.Printf("Answer: %t \n\n", ans)

	nums = []int{1, 2, 3, 4}
	fmt.Printf("Input: %v \n", nums)
	ans = containsDuplicate(nums)
	fmt.Printf("Answer: %t \n\n", ans)

	nums = []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}
	fmt.Printf("Input: %v \n", nums)
	ans = containsDuplicate(nums)
	fmt.Printf("Answer: %t \n\n", ans)

	fmt.Printf("Done running the problem in %s seconds.\n", time.Since(t0))
}

// Given an integer array nums, return true if any value appears at least twice in the array,
// and return false if every element is distinct.
//
// LeetCode: https://leetcode.com/problems/contains-duplicate
func containsDuplicate(nums []int) bool {

	hashMap := make(map[int]struct{})
	for _, v := range nums {
		_, ok := hashMap[v]
		if ok {
			return true
		}
		hashMap[v] = struct{}{}
	}

	return false
}
