from pygorithm.data_structures import stack
from pygorithm.sorting import bubble_sort
from pygorithm.sorting import quick_sort
from pygorithm.sorting import merge_sort
from pygorithm.sorting import selection_sort


# help(data_structures)
# ----------------------------------------------------------------------------------------------------------------------
s = stack.Stack()
code = s.get_code()
print(code)


# ----------------------------------------------------------------------------------------------------------------------
test_list = [1234, 4312, 4, 34, 8903, 0, 67]
bubble_sorted_list = bubble_sort.sort(test_list)
print(bubble_sorted_list)

test_list2 = [32, 4.3, 45, 5, 6, 789]
quick_sorted_list = quick_sort.sort(test_list2)
print(quick_sorted_list)

test_list3 = [32, 33, 4, 35, 116, 7566589]
merge_sorted_list = merge_sort.sort(test_list2)
print(merge_sorted_list)

test_list4 = [32, 33, 4, 35, 116, 7566589]
selection_sorted_list = selection_sort.sort(test_list4)
print(selection_sorted_list)
