#! usr/env/bin Python3 
#TODO- remove redunant fucntions, comment, each function should be a program
# get_file_paths_in_dir_and_subdirs- takes an input path to a directory, and returns all files in the directory and its subdirectories
import sys 
import os
from user_funcs import check_input_type, getuser_str
import shutil, myimports
#--------------------------------------------------------
all_file_paths_in_dirs_and_subdirs = [] # global variable -this allows storing file paths

def get_file_paths_in_dir_and_subdirs(dir_path, verbose = 0):
    """takes an input path to a directory, and returns all
    files in the directory and its subdirectories
    
    strategy
    --------
    -extracts file/folder names from input dir into a list
    -loops list and checks if subdirs exist. If true,
    does recursion, else, appends the aboslute file path to 
    a global variable.the latter is the base case of the recursion.
    *the recursion call allows extraction of files from subdirs,
    subsubdirs...etc
        
    notes
    -----
    -uses:
       os.listdir to extract the names of all files and folders in dir.
       os.path.isdir to check if file/folder is a dir
       os.path.abspath to extract full path of file.
    -handles invalid input type and also when dir is not found.
    
    parameters
    ----------
    dir_path: str
       path to dir
    verbose: 0,1
       set to 1 for debugging 
       
    return
    ------
     list"""
    
    # check_inputs(str, 'your input was not a string', dir_path)
    
    try:
        # extract names of files and folders in dir into a list
        list_of_items_in_folder = os.listdir(dir_path)

        # loops list of names of files and folders, and appends filesnames to a global variable. 
        # does recursion for dirs to extract its file names
        for item in list_of_items_in_folder:
            
            full_item_path = os.path.join(dir_path,item)
            
            if os.path.isdir(full_item_path) == True: # checks if item is a dir
                subdir_path = os.path.join(os.path.abspath(dir_path),item) # extracts full path of item(subdir) to use for recursion
                subdir = get_file_paths_in_dir_and_subdirs(subdir_path)

            else:
                # this is the base case of the recursion
                file = os.path.join(dir_path,item)
                all_file_paths_in_dirs_and_subdirs.append(file) # appends file name to global variable

        return all_file_paths_in_dirs_and_subdirs
    
    except FileNotFoundError:    
        print('your input path does not exist')
# ---------------------------------------------------
def get_file_paths_in_dir_and_subdirs_v2(dir_path, verbose = 0):
    """takes an input path to a directory, and returns all
    files in the directory and its subdirectories
    
    strategy
    --------
    -extracts file/folder names from input dir into a list
    -loops list and checks if subdirs exist. If true,
    does recursion, else, appends the aboslute file path to 
    a global variable.the latter is the base case of the recursion.
    *the recursion call allows extraction of files from subdirs,
    subsubdirs...etc
        
    notes
    -----
    -uses:
       os.listdir to extract the names of all files and folders in dir.
       os.path.isdir to check if file/folder is a dir
       os.path.abspath to extract full path of file.
    -handles invalid input type and also when dir is not found.
    
    parameters
    ----------
    dir_path: str
       path to dir
    verbose: 0,1
       set to 1 for debugging 
       
    return
    ------
     list"""
    
    # check_inputs(str, 'your input was not a string', dir_path)
    all_file_paths_in_dirs_and_subdirs = []
    try:
        # extract names of files and folders in dir into a list
        list_of_items_in_folder = os.listdir(dir_path)

        # loops list of names of files and folders, and appends filesnames to a global variable. 
        # does recursion for dirs to extract its file names
        for item in list_of_items_in_folder:
            
            full_item_path = os.path.join(dir_path,item)
            
            if os.path.isdir(full_item_path) == True: # checks if item is a dir
                # subdir_path = os.path.join(os.path.abspath(dir_path),item) # extracts full path of item(subdir) to use for recursion
                all_file_paths_in_dirs_and_subdirs += get_file_paths_in_dir_and_subdirs(full_item_path)

            else:
                # this is the base case of the recursion
                # file = os.path.join(dir_path,item)
                all_file_paths_in_dirs_and_subdirs.append(file) # appends file name to global variable

        return all_file_paths_in_dirs_and_subdirs
    
    except FileNotFoundError:    
        print('your input path does not exist')
# ---------------------------------------------------
def get_all_paths_in_dir_and_subdirs(dir_path, verbose = 0):
    """takes an input path to a directory, and returns a list
    of all pathsin the directory
    
    strategy
    --------
    -extracts file/folder names from input dir into a list
    -loops list and checks if subdirs exist. If true,
    does recursion, else, appends the aboslute file path to 
    a global variable.the latter is the base case of the recursion.
    *the recursion call allows extraction of files from subdirs,
    subsubdirs...etc
        
    notes
    -----
    -uses:
       os.listdir to extract the names of all files and folders in dir.
       os.path.isdir to check if file/folder is a dir
       os.path.abspath to extract full path of file.
    -handles invalid input type and also when dir is not found.
    
    parameters
    ----------
    dir_path: str
       path to dir
    verbose: 0,1
       set to 1 for debugging 
       
    return
    ------
     list"""
    
    # check_inputs(str, 'your input was not a string', dir_path)
    all_paths_in_dirs_and_subdirs = []
    try:
        # extract names of files and folders in dir into a list
        list_of_items_in_folder = os.listdir(dir_path)

        # loops list of names of files and folders, and appends filesnames to a global variable. 
        # does recursion for dirs to extract its file names
        for item in list_of_items_in_folder:
            
            full_item_path = os.path.join(dir_path,item)
            
            if (os.path.isdir(full_item_path) == True): # checks if item is a dir
                # subdir_path = os.path.join(os.path.abspath(dir_path),item) # extracts full path of item(subdir) to use for recursion
                all_paths_in_dirs_and_subdirs += get_all_paths_in_dir_and_subdirs(full_item_path)
                all_paths_in_dirs_and_subdirs.append(full_item_path)

            else:
                # this is the base case of the recursion
                # file = os.path.join(dir_path,item)
                all_paths_in_dirs_and_subdirs.append(full_item_path) # appends file name to global variable

        return all_paths_in_dirs_and_subdirs
    
    except FileNotFoundError:    
        print('your input path does not exist')
# ---------------------------------------------------
def get_file_paths_w_ext_in_folders(path_to_folder, ext = None):
    
    all_paths = get_all_paths_in_dir_and_subdirs(path_to_folder)
    filtered_paths = []
    
    for path in all_paths:
        if type(ext) == list: # this allows fetching files with different .exts
            for extension in ext:
                if path.endswith(extension):
                    filtered_paths.append(path)
        else:
            path.endswith(ext)
            filtered_paths.append(path)
    
    return filtered_paths
# ---------------------------------------------------

def get_folder_size(input_dir_path, convert_size = False):
    """takes an input path to a directory
    and returns the size of the directory
    
    strategy
    --------
    - loops a list of all files that exist
    in the directory 
    - checks if item in list is a file or folder
    if it is a folder, it does a recursion.
    if it is a file, it sums up size of all 
    files in dir and subdirs (this is the
    base case of the recursion).
    
    note
    ----
    -uses check inputs to handle invalid inputs
    - uses os.scandir to extract a list of all 
    files and subdir that exist in the input_dir_path
    
    parameters
    ----------
    input_dir_path: str
       input dir to get size
    
    returns
    -------
    int"""

    check_inputs(str,'your input was not as string', input_dir_path)
    
    try:
        total_file_size = 0
        # loops list of dirs and files
        for item in os.scandir(input_dir_path):
            # checks if dir is file, if true
            # adds to total file size
            if item.is_dir():
                total_file_size += item.stat().st_size
                total_file_size += get_folder_size(item.path)
                
            
            else:
                total_file_size += item.stat().st_size
            
        if convert_size == True: 
            total_file_size = convert_file_size(total_file_size)
            
        return total_file_size
    
    except NotADirectoryError:
        print('your input was not a directory.')
#---------------------------------------------------------------------
def convert_file_size(input_bytes, verbose = 0):
    """takes an input number and converts number to 
    bytes, KB MB..TB depending on how large the number is 
    
    strategy
    --------
    - makes a list that contains conversion units
    - loops list and checks if input bytes is < or > than
    1024. This number is the upper limit of bytes(KB,MB..etc) to check
    if a conversion will be made to a larger unit. 
     if the input unit is smaller than 1024, a value is 
     returned (this shortciruits the function).
     else the input is divided by 1024 until is lower than
     1024. In this case the function will shortcicuit when
     the loop reaches the relevant unit to convert to. 
    
    parameters
    ----------
    input_bytes: int or float
       number of bytes to convert
    verbose: 0,1
        optional bool, set to 1 for debugging
        
    note
    ----
    uses check inputs to handles invalid inputs
    
    returns
    -------
    str"""
    
    check_inputs([int,float], 'your input was not a number', input_bytes)
    
    # does loop in range of units to convert and checks
    # if greater than 1024 (limit at which to convert unit)
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        
        # if bytes are greater than smaller than 1024, returns bytes and exits loop,
        # else divides the bytes by 1024, until the number is <1024, in 
        # this case the loop will shortcirtuit at the corresponding unit
        if input_bytes < 1024:
            if verbose == 1:
                print('current bytes value: {}'.format(input_bytes))
            
            #could return int or float
            return "%3.1f %s" % (input_bytes, unit) # this returns the number to the first decimal point
        else:
            input_bytes = input_bytes / 1024
#-------------------------------------------------------------------------------------
def get_file_size(input_path, convert_size = True, verbose = 0):
    """takes an input path to a file or folder
    and returns its size. 
    
    notes
    -----
    -creates a file statistics object
    using os.stat and converts the 
    file size attribute to a unit that
    would give the lowest value.
    - uses convert_bytes to get file conver
    os.st_size output.
    - uses check inputs to handles invalid inputs
    
    parameters
    ----------
    input_path: str
       path to file to get size
    verbose: 0,1
        optional bool, set to 1 for debugging
        
    returns
    -------
    str"""
    
    check_inputs(str, 'your input path was not a number', input_path)
    
    try:
        file_info = os.stat(input_path)
        file_size = file_info.st_size
        
        if convert_size == True:
            file_size = convert_file_size(file_info.st_size)
        
        if verbose == 1:
            print('extracted file stats: {}\n converted file size: {}'.format(file_info, converted_file_size))
            
        return file_size
    
    except FileNotFoundError:
        print('your input path was not found.')
#------------------------------------------------
def is_dir(input_path):
    
    return os.path.isdir(input_path)
#------------------------------------------------
def get_file_paths_from_dir(dir_path, ext = None, verbose = 0):
    """takes an input directory and returns
    a list of files in that directory. given
    an input file extension, only files with
    that ext. are included in the list.
    
    parameters
    ----------
    input_cwd: str
       path to directory
    ext: None
       extension to use to filter for file types
    verbose: 0,1
        set to 1 for debugging
    
    returns
    -------
    list"""
    
    # checks if input type is valid
    check_input_type(str,'your input was not a valid type', dir_path)
    
    # get files and folder in cwd
    dir_path = os.path.abspath(dir_path)
    files_folders_in_cwd = os.listdir(dir_path)
    list_of_files = []
    
    # loops over file_folder list and appends file
    # names to list, if ext is specified by the user,
    # only files with the .ext are appended to the list.
    # otherwise, all files are appended to the list.
    for item in files_folders_in_cwd:
        path_to_item = os.path.join(dir_path, item) # allows returning full path of file
        
        if os.path.isfile(path_to_item) == True: 
            if ext != None:    # this allows filtering for files with specific exts.
                
                if type(ext) == list: # this allows fetching files with different .exts
                    for extension in ext:
                        if item.endswith(extension):
                            list_of_files.append(path_to_item)
                else:
                    item.endswith(ext)
                    list_of_files.append(path_to_item)
            else:
                list_of_files.append(path_to_item)

    return list_of_files
#------------------------------------------------
def get_file_paths_from_dir(dir_path, ext = None, verbose = 0):
    """takes an input directory and returns
    a list of files in that directory. given
    an input file extension, only files with
    that ext. are included in the list.
    
    parameters
    ----------
    input_cwd: str
       path to directory
    ext: None
       extension to use to filter for file types
    verbose: 0,1
        set to 1 for debugging
    
    returns
    -------
    list"""
    
    # checks if input type is valid
    check_input_type(str,'your input was not a valid type', dir_path)
    
    # get files and folder in cwd
    dir_path = os.path.abspath(dir_path)
    files_folders_in_cwd = os.listdir(dir_path)
    list_of_files = []
    
    # loops over file_folder list and appends file
    # names to list, if ext is specified by the user,
    # only files with the .ext are appended to the list.
    # otherwise, all files are appended to the list.
    for item in files_folders_in_cwd:
        path_to_item = os.path.join(dir_path, item) # allows returning full path of file
        
        if os.path.isfile(path_to_item) == True: 
            if ext != None:    # this allows filtering for files with specific exts.
                
                if item.endswith(ext):
                    list_of_files.append(path_to_item)
            else:
                list_of_files.append(path_to_item)
                
    return list_of_files
#------------------------------------------------
def get_file_name(file_path):
    return os.path.basename(file_path)
#------------------------------------------------
def copy_files_to_folder(list_of_paths, output_folder):
    """takes an input list of paths and a path to
    an output folder, copies files to folder"""
    
    try:
        os.path.isdir == True
    except AssertionError:
        print('your input dir path was not a directory')    
    check_input_type(list, 'your input list of paths was not a list')
    check_input_type(str, 'your input folder path was not a string')

    for path in list_of_paths:
        file_name = os.path.basename(path)
        new_file_path = os.path.join(output_folder, file_name)
        shutil.copy(path, new_file_path)
        
    print('Done')
#------------------------------------------------
def get_paths_with_substrs(input_path_list, delim1, delim2, list_var):
    
    list_of_paths = []
    
    for path in input_path_list: 
        path_substr, pos = myimports.substring_delim(path, delim1, delim2, 0)
        if path_substr in list_var:
            list_of_paths.append(path)
            
    return list_of_paths
#------------------------------------------------
def copy_file_to_folder(file_path, output_folder, add_ext = None):
    """takes an input list of paths and a path to
    an output folder, copies files to folder"""
    
    try:
        os.path.isdir(output_folder) == True
    except AssertionError:
        print('your input dir path was not a directory')    
        
    try:
        os.path.isfile(file_path) == True
    except AssertionError:
        print('your input file path was not a file')    
        
    #check_input_type(list, 'your input list of paths was not a list')
    #check_input_type(str, 'your input folder path was not a string')

    if type(add_ext) == str:
        path_without_file_ext = os.path.splitext(file_path)[0]
        name = os.path.split(path_without_file_ext)[1]
        ext  = os.path.splitext(file_path)[1]
        file_name = os.path.join(output_folder, name)
        new_file_path = "{}{}{}".format(file_name,add_ext, ext)
        print(file_path)
        print(new_file_path)
        shutil.copy(file_path, new_file_path)
    else:
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(output_folder, file_name)
        shutil.copy(file_path, new_file_path)
#------------------------------------------------        
def copy_files(name_path_tuple, output_dir, add_ext = None):
    
    for name_path in name_path_tuple:
        name = name_path[0]
        path = name_path[1]
        copy_file_to_folder(path, output_dir, add_ext = add_ext)
            
    print('Done')
#------------------------------------------------
def get_mod_fname_from_path(path_to_file, mod):
    
    path_without_file_ext = os.path.splitext(path_to_file)[0]
    name = os.path.split(path_without_file_ext)[1]
    ext = os.path.splitext(path_to_file)[1]
    file_name = "{0}{1}{2}".format(name, mod, ext)
    
    return file_name
#------------------------------------------------
def get_file_paths_from_dir(dir_path, ext = None, verbose = 0):
    """takes an input directory and returns
    a list of files in that directory. given
    an input file extension, only files with
    that ext. are included in the list.
    
    parameters
    ----------
    input_cwd: str
       path to directory
    ext: None
       extension to use to filter for file types
    verbose: 0,1
        set to 1 for debugging
    
    returns
    -------
    list"""
    
    # checks if input type is valid
    check_input_type(str,'your input was not a valid type', dir_path)
    
    # get files and folder in cwd
    dir_path = os.path.abspath(dir_path)
    files_folders_in_cwd = os.listdir(dir_path)
    list_of_files = []
    
    # loops over file_folder list and appends file
    # names to list, if ext is specified by the user,
    # only files with the .ext are appended to the list.
    # otherwise, all files are appended to the list.
    for item in files_folders_in_cwd:
        path_to_item = os.path.join(dir_path, item) # allows returning full path of file
        
        if os.path.isfile(path_to_item) == True: 
            if ext != None:    # this allows filtering for files with specific exts.
                
                if type(ext) == list: # this allows fetching files with different .exts
                    for extension in ext:
                        if item.endswith(extension):
                            list_of_files.append(path_to_item)
                else:
                    item.endswith(ext)
                    list_of_files.append(path_to_item)
            else:
                list_of_files.append(path_to_item)
                
    return list_of_files
#------------------------------------------------
def replace_txt_in_dir_files(dir_path, word_rword_list, verbose = 0):
    """takes an input path to a dir and a list of tuple pairs i.e
    [(word1, replacement_word1) ...etc]. replaces word with replacement 
    for each file in the dir"""
    
    # prints error message if user input is an invalid type
    check_input_type(str, 'your input path was not a string', dir_path)
    check_input_type(list, 'your input tuple list was not a list', word_rword_list)
    
    # prints error message if elements in list are not tuples
    check_item_type(word_rword_list, tuple)
    
    # extracts list of absolute path of each file in dir
    files_in_dir = get_file_paths_from_dir(dir_path)
    if verbose == 1:
        print('list of files in dir: {}'.format(files_in_dir))
        
    # calls replace txt_in_file on each file path
    for file in files_in_dir:
        replace_txt_in_file(file, word_rword_list)
        if verbose == 1:
            print('last file completed {}:'.format(os.path.basename(file))) # os function extracts name of file
            
    print('operation complete: check working dir for output files'.format(dir_path))
#------------------------------------------------
def make_dirs(path_to_dir, dir_name, overwrite_dirs = False, verbose = 0):
    """takes an input path and a name of 
    dir to make. create dir in the input path
    
    process
    -------
    - checks for user invalid inputs
    - concatenates dir_name to path
    - creates dir in path 
    - if dir exists, creates dir_name_1 or overwrites dir (depending on overwrite_dir input)
    - returns path to dir. 
    
    parameters
    ----------
    path_to_dir: str
        path to create the dir
    dir_name: str
        name of dir to create
    overwrite_dirs: bool
        if True, if the dirname already exists, it is overwritten,
        else an error is raised.
 
    returns 
    -------
    str"""
    
    check_input_type(str, 'one or both your inputs were not strings, got {}, {}'.format(type(path_to_dir), type(dir_name)), path_to_dir, dir_name)
    
    try:
        assert os.path.isdir(path_to_dir) == True
    except AssertionError:
        print('your input dir path was not a valid dir path: {}'.format(path_to_dir))
    
    dir_path = os.path.join(path_to_dir, dir_name)
    name_copy_number = 1
    
    if (overwrite_dirs == False) or (overwrite_dirs == 'False'): 
        while os.path.exists(dir_path):
            new_dir_name = "{}_{}".format(dir_name, name_copy_number)
            dir_path = os.path.join(path_to_dir, new_dir_name)
            name_copy_number += 1
                
    os.makedirs(dir_path, exist_ok = overwrite_dirs)
        
    return dir_path
#------------------------------------------------
# function that gets paths to files if they contain a substring
def get_paths_with_substrs(input_path_list, delim1, delim2, list_var):
    """takes an input list of file paths and a list of strings,
    and two input delimiters. returns a list in which file paths
    have the substrings present in the second input list. """
    
    list_of_paths = []
    
    for path in input_path_list: 
        path_substr, pos = myimports.substring_delim(path, delim1, delim2, 0) # extracts substring from file path
        if path_substr in list_var: # checks if substring is in the list
            list_of_paths.append(path) # if True, appends file path, else, nothing
            
    return list_of_paths
#------------------------------------------------
if __name__ == '__main__':
    main()
