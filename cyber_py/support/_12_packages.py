import os

# 记录满足某前缀的txt文件
def get_txts_with_prefix(folder_path, prefix):
    """
    Gets file names with a certain prefix from a given folder path. 
    
    Args:
        folder_path (str): The path to the folder containing the files.
        prefix (str): The prefix to search for in the file names.
    
    Returns:
        list: A list of file paths that match the given prefix and have a .txt extension.
    """
    files = os.listdir(folder_path)
    result = [os.path.join(folder_path, file) for file in files if file.startswith(prefix) and file.endswith('.txt')]
    if not result:
        result.append('Unknown')

    return result

# 按上函数结果读取文件
def read_txts(files):
    """
    Reads the contents of text files and returns a list of their contents.
    
    Args:
        files (list): A list of file paths to read.
    
    Returns:
        list: A list of the contents of the text files.
    """
    result = []
    if files[0] == 'Unknown':
        result.append('Unknown')
    else:
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
                result.append(content)
    return result


#    txts = get_txts_with_prefix(folder_path, prefix)
#    txts = read_txts(txts)