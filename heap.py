import random


def left(i):
    return i * 2


def right(i):
    return i * 2 + 1


def max_heapify(arr, i):
    l = left(i)
    r = right(i)
    largest = i
    if l < len(arr) and arr[l] > arr[largest]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        max_heapify(arr, largest)


def min_heapify(arr, i):
    l = left(i)
    r = right(i)
    smallest = i
    if l < len(arr) and arr[l] < arr[smallest]:
        smallest = l
    if r < len(arr) and arr[r] < arr[smallest]:
        smallest = r
    if i != smallest:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        min_heapify(arr, smallest)


def build_max_heap(arr):
    for i in reversed(range(0, len(arr)//2)):
        max_heapify(arr, i)


def build_min_heap(arr):
    for i in reversed(range(0, len(arr)//2)):
        min_heapify(arr, i)


def heapsort(arr):
    build_max_heap(arr)
    ans = []
    for i in reversed(range(0, len(arr))):
        ans.append(arr[0])
        arr.pop(0)
        max_heapify(arr, 0)

    return ans

if __name__ == '__main__':
    unsorted_arr = random.sample(range(1, 500), 20)
    print("Before Heapify: ", unsorted_arr)
    build_max_heap(unsorted_arr)
    print("After Max Heapify: ", unsorted_arr)
    build_min_heap(unsorted_arr)
    print("After Min Heapify: ", unsorted_arr)
    print()

    # Heap sort
    randomArr = random.sample(range(1, 500), 20)
    print("Before heap sort: ", randomArr)
    sorted_arr = heapsort(randomArr)
    print("After heap sort:  ", sorted_arr)

