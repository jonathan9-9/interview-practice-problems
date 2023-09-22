# SELECTION SORT

def selection_sort(nums):
    for i in range(len(nums)):
        minimum_val_index = i
        for j in range(i + 1, len(nums)):
            if nums[minimum_val_index] > nums[j]:
                minimum_val_index = j
        nums[i], nums[minimum_val_index] = nums[minimum_val_index], nums[i]
    return nums


values = [7, 3, 2, 10, 4, 9, 100, 8, 2, 34, 13, 12, 6, 18]
result = selection_sort(values)
# print(result)

# BUBBLE SORT


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


values = [7, 3, 2, 10, 4, 9, 100, 8, 2, 34, 13, 12, 6, 18]
result = bubble_sort(values)
# print(result)

# QUICK SORT Lomuto's strat


def partition(values, left, right):
    pivot = values[right]
    star = left - 1
    for i in range(left, right):
        if values[i] <= pivot:
            star += 1
            values[star], values[i] = values[i], values[star]
    star += 1
    values[star], values[right] = values[right], values[star]
    return star


def quick_sort(values, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(values) - 1
    if left >= right or left < 0:
        return
    p = partition(values, left, right)
    quick_sort(values, left, p - 1)
    quick_sort(values, p + 1, right)


numbers = [5, 9, 3, 7, 1, 10]
quick_sort(numbers)
print("quicksort:", numbers)



# HEAP SORT

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def siftDown(lst, i, upper):

    while (True):
        l, r = i*2+1, i*2+2
        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]):
                break
            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l
            else:
                swap(lst, i, r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l
            else:
                break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r
            else:
                break
        else:
            break


def heapSort(lst):
    for k in range((len(lst) - 2) // 2, -1, -1):
        siftDown(lst, k, len(lst))

    for end in range(len(lst) - 1, 0, -1):
        swap(lst, 0, end)
        siftDown(lst, 0, end)


values = [7, 10, 55, 23, 40, 78]
heapSort(values)
print("HEAPSORT:", values)
