# https://skillsmart.ru/algo/15-121-cm/e858048f95.html

def ArrayChunk(array, left, right):
    i = left
    j = right
    N = len(array[i:j+1])//2 + i
    while True:
        if array[i] < array[N]:
            i += 1
        if array[j] > array[N]:
            j -= 1
        if i == j-1 and array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
            return ArrayChunk(array, left, right)
        if i == j or (i == j-1 and array[i] < array[j]):
            return N
        if array[i] >= array[N] and array[j] <= array[N]:
            array[i], array[j] = array[j], array[i]
            if i == N:
                N = j
            elif j == N:
                N = i

def QuickSort(array, left, right):
    if left < right:
        middle = ArrayChunk(array, left, right)
        QuickSort(array, left, middle-1)
        QuickSort(array, middle+1, right)
