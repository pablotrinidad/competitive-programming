package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
	"strings"
)

func computeDistances(arr []int32) (distances map[int]int) {
	distances = make(map[int]int)
	for i := range arr {
		distances[i] = int(math.Abs(float64(i+1) - float64(arr[i])))
	}
	return distances
}

func getOptimumSwap(distances map[int]int, arr []int32) (pair []int) {
	indexes := []int{}
	// Use only numbers out of position, i.e.: distance to position is not 0
	for k, v := range distances {
		if v > 0 {
			indexes = append(indexes, k)
		}
	}

	// Compute combinations len(indexes) on 2: O(n^2)
	minSoFar := len(arr) * 2
	for i, IthIndex := range indexes {
		for j := i + 1; j < len(indexes); j++ {
			JthIndex := indexes[j]
			currentDistance := distances[IthIndex] + distances[JthIndex]
			distanceAfterSwap := (int(math.Abs(float64(JthIndex+1)-float64(arr[IthIndex]))) +
				int(math.Abs(float64(IthIndex+1)-float64(arr[JthIndex]))))
			if distanceAfterSwap-currentDistance <= minSoFar {
				minSoFar = distanceAfterSwap - currentDistance
				pair = []int{IthIndex, JthIndex}
			}
		}
	}
	return pair
}

// Complete the minimumSwaps function below.
func minimumSwaps(arr []int32) (swaps int32) {
	distances := computeDistances(arr)
	pair := getOptimumSwap(distances, arr)
	for len(pair) == 2 {
		arr[pair[0]], arr[pair[1]] = arr[pair[1]], arr[pair[0]]
		distances = computeDistances(arr)
		pair = getOptimumSwap(distances, arr)
		swaps++
	}
	return swaps
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 1024*1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	n := int32(nTemp)

	arrTemp := strings.Split(readLine(reader), " ")

	var arr []int32

	for i := 0; i < int(n); i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}

	res := minimumSwaps(arr)

	fmt.Fprintf(writer, "%d\n", res)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
