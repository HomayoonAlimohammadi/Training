package anagram

import (
	"fmt"
	"reflect"
	"time"
)

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
//
// An Anagram is a word or phrase formed by rearranging the letters of a different word
// or phrase, typically using all the original letters exactly once.
//
// LeetCode: https://leetcode.com/problems/valid-anagram/
func IsValid() {
	t0 := time.Now()
	fmt.Println()
	fmt.Println("Running Valid Anagram...")
	fmt.Println()

	s := "anagram"
	t := "nagaram"
	fmt.Println("Input:", s, t)
	ans := isAnagramImplOne(s, t)
	fmt.Println("Answer 1:", ans)
	ans = isAnagramImplTwo(s, t)
	fmt.Println("Answer 2:", ans)
	fmt.Println()

	s = "rat"
	t = "car"
	fmt.Println("Input:", s, t)
	ans = isAnagramImplOne(s, t)
	fmt.Println("Answer 1:", ans)
	ans = isAnagramImplTwo(s, t)
	fmt.Println("Answer 2:", ans)
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.", time.Since(t0))
	fmt.Println()
}

func isAnagramImplOne(s string, t string) bool {
	sMap := make(map[rune]int)
	tMap := make(map[rune]int)

	for _, v := range s {
		sMap[v] = sMap[v] + 1
	}

	for _, v := range t {
		tMap[v] = tMap[v] + 1
	}

	return reflect.DeepEqual(sMap, tMap)
}

type Node struct {
	value interface{}
	prev  *Node
}

type Stack struct {
	head   *Node
	length int
}

func (s *Stack) Peek() interface{} {
	if s.length == 0 {
		return nil
	}

	return s.head.value
}

func (s *Stack) Push(value interface{}) {
	newNode := &Node{value: value, prev: s.head}
	s.head = newNode
	s.length++
}

func (s *Stack) Pop() interface{} {
	if s.length == 0 {
		return nil
	}

	val := s.head.value
	s.head = s.head.prev
	s.length--

	return val
}

// This does not work. Just an experimental thing.
func isAnagramImplTwo(s string, t string) bool {
	var i, j int
	st := &Stack{}

	for i < len(s) && j < len(t) {
		if s[i] == t[j] {
			i++
			j++
		} else if top := st.Peek(); top != nil && top == s[i] {
			_ = st.Pop()
			i++
		} else {
			st.Push(t[j])
			j++
		}
	}

	if i == len(s) && j == len(t) {
		return true
	}
	return false
}
