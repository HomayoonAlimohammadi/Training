package sentence

import (
	"fmt"
	"time"
)

// Given a string s consisting of words and spaces,
// return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.
//
// LeetCode: https://leetcode.com/problems/length-of-last-word/
func LengthOfLastWord() {
	t0 := time.Now()
	fmt.Println()
	fmt.Println("Running Length of last word...")
	fmt.Println()

	s := "Hello World"
	fmt.Println("Input:", s)
	ans := lengthOfLastWord(s)
	fmt.Println("Answer 1:", ans)
	fmt.Println()

	s = "   fly me   to   the moon  "
	fmt.Println("Input:", s)
	ans = lengthOfLastWord(s)
	fmt.Println("Answer 1:", ans)
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.", time.Since(t0))
	fmt.Println()
}

func lengthOfLastWord(s string) int {
	var l int
	for i := len(s) - 1; i >= 0; i-- {
		if string(s[i]) != " " {
			l++
		} else if string(s[i]) == " " && l != 0 {
			break
		}
	}

	return l
}
