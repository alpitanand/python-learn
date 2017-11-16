import os

# listing = os.walk('.')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)


def dir_list(s):
    nonlocal tab_stop
    files = os.listdir(s)
    for numFile in files:
        current_dir = os.path.join(s, numFile)
        if os.path.isdir(current_dir):
            print('\t'*tab_stop + 'Directory '+numFile)
            tab_stop += 1

tab_stop = 1


def list_directories(s):
    if os.path.exists(s):
        print("Directory listing of "+s)
        dir_list(s)
    else:
        print("Directory does not exist")



