def selection_algor(nums):
    #  i -> кількість відсортованих значень
    for i in range(len(nums)):
        lowest_value_index = i  # допустимо, що найменший елемент- перший
        for j in range(i + 1, len(nums)):  # перебірка несортованих елементів
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]  # найменший міняємо з першим елементом


random_list_of_nums = [12, 8, 3, 20, 11]
selection_algor(random_list_of_nums)
print(random_list_of_nums)
