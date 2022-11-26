package main

import (
	"fmt"
	"math/rand"
	"time"
)

func makeListCircular(list []string) {
	tempList := shuffleList(list, 7)
	for i, person := range tempList {
		if i == len(tempList)-1 {
			fmt.Printf("%s with %s \n", person, tempList[1])
			return
		}
		fmt.Printf("%s with %s \n", person, tempList[i+1])
	}
}
func splitList(list []string, chuckSize int) [][]string {
	splittedArray := [][]string{}
	tempArray := []string{}

	for i, item := range list {
		if i%chuckSize == 0 && i != 0 {
			splittedArray = append(splittedArray, tempArray)
			tempArray = []string{}
		}
		tempArray = append(tempArray, item)
		if i == len(list)-1 {
			splittedArray = append(splittedArray, tempArray)
		}
	}
	return splittedArray
}
func makeListPartnered(list []string, numOfPartners int, oddPartner string) [][]string {
	shuffledList := shuffleList(list, len(list))
	divided_list := splitList(shuffledList, numOfPartners)
	if len(divided_list[len(divided_list)-1]) <= 1 {
		divided_list[len(divided_list)-1] = append(divided_list[len(divided_list)-1], oddPartner)
	}
	return divided_list
}

func shuffleList(list []string, swapNum int) []string {
	for i := 0; i < swapNum; i++ {
		currentPos := i
		//rand.Seed(time.Now().UnixMilli())
		randNum2 := randIndexFromSlice(list)
		if currentPos == randNum2 {
			i = i - 1
			continue
		}
		temp := list[currentPos]
		list[currentPos] = list[randNum2]
		list[randNum2] = temp
	}
	return list
}

func randIndexFromSlice(list []string) int {
	rand.Seed(time.Now().UnixNano())
	randNum := 1 + rand.Intn(len(list)-1)
	return randNum
}

func pretiffyList(list [][]string) {
	for _, item := range list {
		fmt.Printf("%s with %s \n", item[0], item[1])
	}
}

func main() {
	fmt.Println("Hey Prayer Partner List Maker")
	fmt.Println("------------------------------")
	peopleList := []string{"Stephan", "Rasheed", "Aisha", "Yordi",
		"Kelly", "Cailin", "Landi", "Tina", "Sophia", "Anita", "Gaberial",
		"Estera", "Joshua", "Priti", "Samuel", "Chantelle", "Mirian", "Balveet"}
	list := makeListPartnered(peopleList, 2, "Stephan")
	pretiffyList(list)
	fmt.Println("------------------------------")
}
