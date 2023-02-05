package slices

import (
	"fmt"
	"sort"
	"time"
)

// Given an integer array nums and an integer k,
// return the k most frequent elements.
// You may return the answer in any order.
//
// LeetCode: https://leetcode.com/problems/top-k-frequent-elements/
func TopKFrequent() {
	t0 := time.Now()
	fmt.Println("Running Contains Duplicate...")

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
