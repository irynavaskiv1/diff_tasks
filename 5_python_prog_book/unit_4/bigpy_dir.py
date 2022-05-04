import os
import glob
import sys

dir_name = r'/Users/admin/Documents/diff_tasks/5_python_prog_book/unit_3' if len(sys.argv) == 1 else sys.argv[1]

all_sizes = []

allpy = glob.glob(dir_name + os.sep + '*.py')

for file_name in allpy:
    file_size = os.path.getsize(file_name)
    all_sizes.append((file_size, file_name))
print(f'All files in {dir_name}, are: {allpy}')

all_sizes.sort()
print(f'All sorted files are: {all_sizes}')
