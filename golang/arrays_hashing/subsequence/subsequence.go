package subsequence

import (
	"fmt"
	"time"
)

// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
//
// A subsequence of a string is a new string that is formed from the original string
// by deleting some (can be none) of the characters without disturbing
// the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
//
// LeetCode: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
func Is() {
	t0 := time.Now()
	fmt.Println()
	fmt.Println("Running Is Subsequence...")
	fmt.Println()

	s := "abc"
	t := "ahbgdc"
	fmt.Println("Input:", s, t)
	ans := isSubsequence(s, t)
	fmt.Println("Answer 1:", ans)
	fmt.Println()

	s = "axc"
	t = "ahbgdc"
	fmt.Println("Input:", s, t)
	ans = isSubsequence(s, t)
	fmt.Println("Answer 1:", ans)
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.", time.Since(t0))
	fmt.Println()
}

func isSubsequence(s, t string) bool {
	var i, j int

	for i < len(s) && j < len(t) {
		if s[i] == t[j] {
			i++
		}
		j++
	}

	return i >= len(s)
}
