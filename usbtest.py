import os.path

def diff(list1, list2):
    return [item for item in list1 if item not in list2]

def foo():
    print("New dive introduced")

def ham():
    print("Drive disconnected")

dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = [f'{d}:' for d in dl if os.path.exists(f'{d}:')]
print(drives)
while True:
    uncheckeddrives = [f'{d}:' for d in dl if os.path.exists(f'{d}:')]
    if x := diff(uncheckeddrives, drives):
        print(f"New drives:     {str(x)}")
        foo()
    if x := diff(drives, uncheckeddrives):
        print(f"Removed drives: {str(x)}")
        ham()
    #drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    drives = uncheckeddrives
