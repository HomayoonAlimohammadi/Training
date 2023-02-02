package main

import (
	"fmt"
	"training/arrays_hashing/anagram"
	"training/arrays_hashing/duplicate"
	"training/arrays_hashing/replace"
)

func main() {

	var q string

Loop:
	for {
		fmt.Println("Input the number of problem you are looking for:\n" +
			"0. Exit \n" +
			"1. Contains Duplicate \n" +
			"2. Valid Anagram \n" +
			"3. Replace Elements with Greatest Element on Right Side")
		fmt.Scanln(&q)

		switch q {
		case "0":
			fmt.Println("Good Bye!")
			break Loop
		case "1":
			duplicate.ContainsDuplicate()
			break Loop
		case "2":
			anagram.IsValid()
			break Loop
		case "3":
			replace.Elements()
			break Loop
		default:
			fmt.Println("Invalid problem number, try again...")
		}
	}

}
