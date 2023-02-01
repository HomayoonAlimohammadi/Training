package main

import (
	"fmt"
	"training/arrays_hashing/duplicate"
)

func main() {

	var q string

Loop:
	for {
		fmt.Println("Input the number of problem you are looking for:\n" +
			"1. Contains Duplicate")
		fmt.Scanln(&q)

		switch q {
		case "1":
			duplicate.ContainsDuplicate()
			break Loop
		default:
			fmt.Println("Invalid problem number, try again...")
		}
	}

}
