package slices

import (
	"fmt"
	"sort"
	"time"
)

// Given an integer array nums, return an array answer such that answer[i]
// is equal to the product of all the elements of nums except nums[i].
//
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
//
// You must write an algorithm that runs in O(n) time and without using the division operation.
//
// LeetCode: https://leetcode.com/problems/product-of-array-except-self/
func ProductExceptSelf() {
	t0 := time.Now()
	fmt.Println("Running Product Except Self...")

	nums := []int{1, 2, 3, 4}
	exp := []int{24, 12, 8, 6}
	fmt.Println("\nInput:", nums)
	fmt.Println("Answer:", productExceptSelf(nums), "Expected:", exp)
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.\n", time.Since(t0))
}

// Given an integer array nums and an integer k,
// return the k most frequent elements.
// You may return the answer in any order.
//
// LeetCode: https://leetcode.com/problems/top-k-frequent-elements/
func TopKFrequent() {
	t0 := time.Now()
	fmt.Println("Running Top K Frequent...")

	nums := []int{1, 2, 2, 3, 1}
	k := 2
	fmt.Println("\nInput:", nums, k)
	fmt.Println("Answer:", topKFrequent(nums, k))
	fmt.Println("Answer 2:", topKFrequentImplTwo(nums, k))
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.\n", time.Since(t0))
}

func topKFrequent(nums []int, k int) []int {
	freqMap := make(map[int]int)
	for _, v := range nums {
		freqMap[v]++
	}

	freqs := []int{}
	for _, f := range freqMap {
		freqs = append(freqs, f)
	}

	sort.Ints(freqs)
	sort.Sort(sort.Reverse(sort.IntSlice(freqs)))

	ans := []int{}
	for i := 0; i < k; i++ {
		for n, f := range freqMap {
			if f == freqs[i] && !contains(ans, n) {
				ans = append(ans, n)
				break
			}
		}
	}

	return ans
}

// Because slices.Contains (external package) is not supported in LeetCode env
func contains(s []int, e int) bool {
	for _, v := range s {
		if v == e {
			return true
		}
	}

	return false
}

func topKFrequentImplTwo(nums []int, k int) []int {
	fMap := make(map[int]int)
	for _, n := range nums {
		fMap[n]++
	}

	bucket := make([][]int, len(nums)+1)
	for n, f := range fMap {
		bucket[f] = append(bucket[f], n)
	}

	topKF := []int{}
	for i := len(bucket) - 1; i > 0; i-- {
		subBuck := bucket[i]
		for _, n := range subBuck {
			topKF = append(topKF, n)
			if len(topKF) == k {
				return topKF
			}
		}
	}

	return topKF
}

func productExceptSelf(nums []int) []int {
	ans := []int{}

	prod := 1
	for _, v := range nums {
		ans = append(ans, prod)
		prod = prod * v
	}

	prod = 1
	for i := range nums {
		ans[len(ans)-i-1] = ans[len(ans)-i-1] * prod
		prod = prod * nums[len(nums)-i-1]
	}

	return ans
}
