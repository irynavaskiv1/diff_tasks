def insertion_sort(nums):
    for i in range(1, len(nums)):  # починаємо з 2-го елемента, думаємо, що 1 відсортований
        item_to_insert = nums[i]   # зберігаємо посилання на попередній елемент
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert: # ел-ти відсортованого ел сунемо вперед, якщо він > ел для вставки
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert  # вставляємо елемент


random_list_of_nums = [9, 1, 15, 28, 6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)
