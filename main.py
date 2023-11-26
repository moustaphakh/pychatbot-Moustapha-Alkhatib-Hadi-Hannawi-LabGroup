#imports used in the code
import os

#list_of_files function creates a list of the current files with the given extension in a certain directory
def list_of_files(directory, extension):
    """this function creates a list of the current files with the given extension in a certain directory
    @directory : str, the directory of which you want to create a list from
    @extension : str, the extension of the filename"""
    files_names = []   
    for filename in os.listdir(directory):    
        if filename.endswith(extension):     
            files_names.append(filename)   
    return files_names




