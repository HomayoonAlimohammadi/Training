package replace

import (
	"fmt"
	"time"
)

// Given an array arr, replace every element in that array with the greatest
// element among the elements to its right, and replace the last element with -1.
//
// After doing so, return the array.
//
// LeetCode: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
func Elements() {
	t0 := time.Now()
	fmt.Println()
	fmt.Println("Running Replace Elements...")
	fmt.Println()

	arr := []int{17, 18, 5, 4, 6, 1}
	fmt.Println("Input:", arr)
	ans := replaceElements(arr)
	fmt.Println("Answer 1:", ans)
	fmt.Println()

	arr = []int{400}
	fmt.Println("Input:", arr)
	ans = replaceElements(arr)
	fmt.Println("Answer 1:", ans)
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.", time.Since(t0))
	fmt.Println()
}

func replaceElements(arr []int) []int {
	bigRight := -1
	for i := len(arr) - 1; i >= 0; i-- {
		tmp := arr[i]
		arr[i] = bigRight
		if tmp > bigRight {
			bigRight = tmp
		}
	}

	return arr
}
