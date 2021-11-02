def insertion_algor(nums):
    """
    This sorting method like select a card and insert to correct position.
    :param nums: list
    :return: sorted list
    """
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


random_list_of_nums = [9, 1, 15, 28, 6]
insertion_algor(random_list_of_nums)
print(random_list_of_nums)
