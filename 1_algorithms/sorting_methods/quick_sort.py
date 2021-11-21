def partition(nums, low, high):
    """
    It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
    according to whether they are less than or greater than the pivot.
    """
    pivot = nums[(low + high) // 2]  # choose a support element (choose the middle, you can first or last)
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)
