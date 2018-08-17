# coding=utf-8
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        privo = array[0]
        less = [i for i in array[1:] if i < privo]
        greater = [j for j in array[1:] if j >= privo]
        return quicksort(less) + [privo] + quicksort(greater)


if __name__ == "__main__":
    print(quicksort([2, 2, 4, 9, 0]))
