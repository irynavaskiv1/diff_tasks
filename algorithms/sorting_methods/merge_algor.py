def merge_algor(myList):
    if len(myList) > 1:
        mid = len(myList) // 2  # визначаємо опорну точку
        left = myList[:mid]
        right = myList[mid:]

        merge_algor(left)
        merge_algor(right)

        i = 0
        j = 0
        k = 0  # ітерація по головному лісту

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1  # рухаємося по наступному слоті

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


random_list_of_nums = [12, 8, 3, 20, 11]
merge_algor(random_list_of_nums)
print(random_list_of_nums)
