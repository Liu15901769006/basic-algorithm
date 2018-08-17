# coding=utf-8


def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


if __name__ == '__main__':
    arr = [5, 3, 6, 2, 10]
    print(selectionsort(arr))
