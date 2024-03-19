import random

def bubbleSort(arr):
    for i in range(len(arr) + 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr

def createList():
    randomList = random.sample(range(1, 100), int(input("Enter the length of the list to generate and sort: ")))
    print("Generated this list: \n", randomList)
    return randomList

print("Sorted List: \n", bubbleSort(createList()))