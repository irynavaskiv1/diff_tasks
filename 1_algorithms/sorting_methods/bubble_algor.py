def bubble_algor(nums):
    """
    Is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if
    they are in the wrong order.
    """
    flag = True
    while flag:
        flag = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = (
                    nums[i + 1],
                    nums[i],
                )  # swipe two numbers -> the main idea of algor
                flag = True


random_list_of_nums = [5, 2, 1, 8, 4]
bubble_algor(random_list_of_nums)
print(random_list_of_nums)
