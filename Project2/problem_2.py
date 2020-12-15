# File Recursion

from os.path import isdir, isfile, join
from os import listdir, getcwd

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    suffix_paths = list()  # Create a list to store path names of files with suffix

    return return_find_files(suffix, path, suffix_paths)  # Pass list to recursive function

def return_find_files(suffix, path, path_list):

    for item in listdir(path):  # Iterate through files in path
        new_path = join(path, item)  # reconstruct complete path name
        # print("item:{}\nis file?:{}\nis directory?:{}".format(item,isfile(new_path),isdir(new_path)))
        if isfile(new_path) and new_path.endswith(suffix):  # Check for suffix
            path_list.append(new_path)
        elif isdir(new_path):  # Recursive call when finding subdirectories
            return_find_files(suffix, new_path, path_list)

    return path_list


suffix = ".c"
path = getcwd()

print(find_files(suffix, path))

# Sample Directory Structure
# ./testdir
# ./testdir/subdir1
# ./testdir/subdir1/a.c
# ./testdir/subdir1/a.h
# ./testdir/subdir2
# ./testdir/subdir2/.gitkeep
# ./testdir/subdir3
# ./testdir/subdir3/subsubdir1
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir4
# ./testdir/subdir4/.gitkeep
# ./testdir/subdir5
# ./testdir/subdir5/a.c
# ./testdir/subdir5/a.h
# ./testdir/t1.c
# ./testdir/t1.h

# Solution
# ./testdir/subdir1/a.c
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir5/a.c
# ./testdir/t1.c