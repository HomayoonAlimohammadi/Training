package sudoku

import (
	"fmt"
	"strings"
	"time"
)

// Determine if a 9 x 9 Sudoku board is valid.
// Only the filled cells need to be validated according to the following rules:
//
// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
//
// Note:
//
// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.
//
// LeetCode: https://leetcode.com/problems/valid-sudoku/
func IsValid() {
	t0 := time.Now()
	fmt.Println("Running Is Valid Sudoku...")

	board := [][]byte{
		[]byte("53..7...."),
		[]byte("6..195..."),
		[]byte(".98....6."),
		[]byte("8...6...3"),
		[]byte("4..8.3..1"),
		[]byte("7...2...6"),
		[]byte(".6....28."),
		[]byte("...419..5"),
		[]byte("....8..79"),
	}
	exp := true
	fmt.Println("\nInput:", board)
	fmt.Println("Answer:", isValidSudoku(board), "Expected:", exp)
	fmt.Println()

	fmt.Printf("Done running the problem in %s seconds.\n", time.Since(t0))
}

func isValidSudoku(board [][]byte) bool {

	// check row, make transposed and squares
	squares := [9][]string{}
	transposed := [9][9]string{}
	for i, bRow := range board {

		row := strings.Split(string(bRow), "")

		// update transposed
		for j, col := range row {
			transposed[j][i] = col

			// update squares
			if i <= 2 {
				if j <= 2 {
					// upper left square
					squares[0] = append(squares[0], col)
				} else if j <= 5 {
					squares[3] = append(squares[3], col)
				} else {
					squares[6] = append(squares[6], col)
				}
			} else if i <= 5 {
				if j <= 2 {
					// upper mid square
					squares[1] = append(squares[1], col)
				} else if j <= 5 {
					squares[4] = append(squares[4], col)
				} else {
					squares[7] = append(squares[7], col)
				}
			} else {
				if j <= 2 {
					// upper right square
					squares[2] = append(squares[2], col)
				} else if j <= 5 {
					squares[5] = append(squares[5], col)
				} else {
					squares[8] = append(squares[8], col)
				}
			}
		}

		// check for duplicates in row
		if containsDuplicateNumber(row) {
			return false
		}
	}

	// check column
	for _, row := range transposed {
		if containsDuplicateNumber(row[:]) {
			return false
		}
	}

	// check square
	for _, row := range squares {
		if containsDuplicateNumber(row) {
			return false
		}
	}

	return true
}

func containsDuplicateNumber(ss []string) bool {
	mem := []string{}
	for _, s := range ss {
		if s == "." {
			continue
		}
		if contains(mem, s) {
			return true
		}
		mem = append(mem, s)
	}

	return false
}

// Because slices.Contains (external package) is not supported in LeetCode env
func contains(s []string, e string) bool {
	for _, v := range s {
		if v == e {
			return true
		}
	}

	return false
}
