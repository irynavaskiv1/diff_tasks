def selection_algor(nums):
    """
    У цьому алгоритмі список (або масив) ділиться на дві частини: список з відсортованими елементами і
    список з елементами, які тільки потрібно сортувати. Спочатку шукається найменший елемент у другому.
    Він додається в кінці першого. Таким чином алгоритм поступово формує список від меншого до більшого.
    """
    #  i -> кількість відсортованих значень
    for i in range(len(nums)):
        lowest_value_index = i  # допустимо, що найменший елемент- перший
        for j in range(i + 1, len(nums)):  # перебірка несортованих елементів
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = (
            nums[lowest_value_index],
            nums[i],
        )  # найменший міняємо з першим елементом


random_list_of_nums = [12, 8, 3, 20, 11]
selection_algor(random_list_of_nums)
print(random_list_of_nums)


# _______________________________________________________________________________________________________________________
def findSmallest(inputes_list):
    smallest = inputes_list[0]
    smallest_index = 0
    for index in range(1, len(inputes_list)):
        if inputes_list[index] < smallest:
            smallest = inputes_list[index]
            smallest_index = index
    return smallest_index


def selection_sort(input_list):
    new_list = []
    for i in range(len(input_list)):
        smallest = findSmallest(input_list)
        new_list.append(input_list.pop(smallest))
    return new_list


print(selection_sort([2, 6, 12, 10]))
