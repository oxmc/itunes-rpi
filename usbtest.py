import os.path

def diff(list1, list2):
    list_difference = [item for item in list1 if item not in list2]
    return list_difference

def foo():
    print("New dive introduced")

def ham():
    print("Drive disconnected")

dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
print(drives)
while True:
    uncheckeddrives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    x = diff(uncheckeddrives, drives)
    if x:
        print("New drives:     " + str(x))
        foo()
    x = diff(drives, uncheckeddrives)
    if x:
        print("Removed drives: " + str(x))
        ham()
    #drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    drives = uncheckeddrives
