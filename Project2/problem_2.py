# File Recursion

from os.path import isdir, isfile, join, split
from os import listdir, getcwd


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    suffix_paths = list()  # Create a list to store path names of files with suffix
    if not isdir(path) and not isfile(path):  # not a valid path
        return None
    elif isfile(path):  # path is a file; pass only directory as path to helper
        path, file = split(path)

    return return_find_files(suffix, path, suffix_paths)  # Pass list to recursive function


def return_find_files(suffix, path, path_list):
    """
    Recursive helper to access all sub-folders in a path.
    :param suffix: A string of target suffix.
    :param path: A string of the path of the file system.
    :param path_list: A list of paths that match target suffix.
    :return: A list of all paths that match target suffix.
    """

    for item in listdir(path):  # Iterate through files in path
        new_path = join(path, item)  # reconstruct complete path name
        if isfile(new_path) and new_path.endswith(suffix):  # Check for suffix
            path_list.append(new_path)
        elif isdir(new_path):  # Recursive call when finding subdirectories
            return_find_files(suffix, new_path, path_list)

    return path_list


if __name__ == "__main__":
    suffixes = [".c",
                ".gitkeep",
                ".exe",
                ""]
    paths = [getcwd(),
             '',
             'banana',
             getcwd() +'\\testdir\subdir1\\a.c']

    for suffix in suffixes:
        print("File paths with suffix r'{}': \n{}\n".format(suffix, find_files(suffix, paths[0])))

    for path in paths:
        print("'{}' file paths from root '{}': \n{}\n".format(suffixes[0], path, find_files(suffixes[0], path)))

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
