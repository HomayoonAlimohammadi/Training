package sum

import (
	"fmt"
	"time"
)

// Given an array of integers nums and an integer target,
// return indices of the two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.
// You can return the answer in any order
//
// LeetCode: https://leetcode.com/problems/two-sum/
func Two() {
	t0 := time.Now()
	fmt.Println()
	fmt.Println("Running Two Sums...")
	fmt.Println()

	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println("Input:", nums, target)
	ans := twoSum(nums, target)
	fmt.Println("Answer 1:", ans)
	fmt.Println("Answer 2:", twoSumImplTwo(nums, target))
	fmt.Println()

	nums = []int{3, 2, 4}
	target = 6
	fmt.Println("Input:", nums, target)
	ans = twoSum(nums, target)
	fmt.Println("Answer 1:", ans)
	fmt.Println("Answer 2:", twoSumImplTwo(nums, target))
	fmt.Println()

	nums = []int{3, 3}
	target = 6
	fmt.Println("Input:", nums, target)
	ans = twoSum(nums, target)
	fmt.Println("Answer 1:", ans)
	fmt.Println("Answer 2:", twoSumImplTwo(nums, target))
	fmt.Println()

	nums = []int{1, 3, 4, 2}
	target = 6
	fmt.Println("Input:", nums, target)
	ans = twoSum(nums, target)
	fmt.Println("Answer 1:", ans)
	fmt.Println("Answer 2:", twoSumImplTwo(nums, target))
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.", time.Since(t0))
	fmt.Println()
}

func twoSum(nums []int, target int) []int {

	// maps <value>:[]<index>
	m := make(map[int][]int)

	for idx, val := range nums {
		m[val] = append(m[val], idx)
	}

	for val, idx := range m {
		remain := target - val
		if remain == val {
			if len(idx) > 1 {
				return idx[:2]
			}
			continue
		}
		otherIdx, ok := m[remain]
		if ok {
			return []int{idx[0], otherIdx[0]}
		}
	}
	return []int{}
}

func twoSumImplTwo(nums []int, target int) []int {
	m := make(map[int]int)

	for i, val := range nums {
		comp := target - val

		if j, exists := m[comp]; exists {
			return []int{i, j}
		}

		m[val] = i
	}

	// useless but necessary
	return []int{}
}
