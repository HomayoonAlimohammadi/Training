package main

import (
	"fmt"

	"github.com/homayoonalimohammadi/training/golang/training/arrays_hashing/anagram"
	"github.com/homayoonalimohammadi/training/golang/training/arrays_hashing/duplicate"
	"github.com/homayoonalimohammadi/training/golang/training/arrays_hashing/replace"
	"github.com/homayoonalimohammadi/training/golang/training/arrays_hashing/sentence"
	"github.com/homayoonalimohammadi/training/golang/training/arrays_hashing/slices"
	"github.com/homayoonalimohammadi/training/golang/training/arrays_hashing/subsequence"
	"github.com/homayoonalimohammadi/training/golang/training/arrays_hashing/sum"
)

func main() {

	var q string

Loop:
	for {
		fmt.Println("Input the number of problem you are looking for:\n" +
			"0. Exit \n" +
			"1. Contains Duplicate \n" +
			"2. Valid Anagram \n" +
			"3. Replace Elements with Greatest Element on Right Side \n" +
			"4. Is Subsequence \n" +
			"5. Length of Last Word \n" +
			"6. Two Sum \n" +
			"7. Group Anagrams \n" +
			"8. Top K Frequent Elements")
		fmt.Scanln(&q)

		switch q {
		case "0":
			fmt.Println("Good Bye!")
			break Loop
		case "1":
			duplicate.Contains()
			break Loop
		case "2":
			anagram.IsValid()
			break Loop
		case "3":
			replace.Elements()
			break Loop
		case "4":
			subsequence.Is()
			break Loop
		case "5":
			sentence.LengthOfLastWord()
			break Loop
		case "6":
			sum.Two()
			break Loop
		case "7":
			anagram.Group()
			break Loop
		case "8":
			slices.TopKFrequent()
			break Loop
		default:
			fmt.Println("Invalid problem number, try again...")
		}
	}

}
