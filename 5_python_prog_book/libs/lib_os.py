import os

print("os.listdir('.') :", os.listdir('.'))
print("os.listdir(b'.') :", os.listdir(b'.'))
print('')

for (dir, subs, files) in os.walk('/Users/admin/Documents/diff_tasks/5_python_prog_book'):
    try:
        print(dir)
    except UnicodeEncodeError:
        print(dir.encode())
