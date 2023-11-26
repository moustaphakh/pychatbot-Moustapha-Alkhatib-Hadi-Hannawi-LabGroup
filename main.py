#imports used in the code
import os,string,math

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

#speeches is a list of the files in the directory speeches
speeches = list_of_files("speeches",'txt')


#extract_president_names function extracts the names of the presidents from the speech txt files names
def extract_president_names():
    """this function extracts the names of the presidents from the speech text files"""
    president_names = set()
    for text in speeches:
        if text[-5] == '1' or text[-5] == '2':
            president_names.add(text[11:-5])
        else:
            president_names.add(text[11:-4])
    president_names = list(president_names)
    return president_names

#last_names is a list containing the names of the presidents by extracting the names from the speech filenames
last_names = extract_president_names()

#this function creates a dictionary associating each president's first name with his last
def associate_first_names():
    """this function creates a dictionary that associates to each president his first and last name"""
    names = {
        'Chirac': 'Jacques',
        'Giscard dEstaing': 'Valery',
        'Mitterrand': 'Francois',
        'Macron': 'Emmanuel',
        'Sarkozy': 'Nicolas',
        'Hollande' :'Francois'
    }

    return {president: names[president] for president in last_names}
#full_names is a dictionary of the presidents first and last names
full_names = associate_first_names()

#this function displays the names of the presidents
def display_names():
    """this function displays the names of the presidents"""
    for name in full_names:
        print(full_names[name],name)

#this function converts all the text from each txt file in speeches from uppercase to lowercase into the folder Clean
def clean_txt():
    """this function takes the text files in speeches, reads them and converts every uppercase letter to a lowercase and creates a Clean folder in the main directory storing the copy of the speeches files in lowercase"""
    #creates the clean folder in your working directory
    if "Clean" not in os.listdir():
        os.mkdir("Clean")

    #dictionary with ascii of ' and - used to translate them to a space
    chrctrs = {13:0,7:0}
    #reads each file respectively and writes a clean copy in clean folder
    for i in speeches:
        with open(f"speeches\\{i}","r",encoding="utf-8") as input:
            with open(f"Clean\\{i}","w",encoding="utf-8") as output:
                for line in input:
                    lowered_line = line.lower()
                    cleaned = lowered_line.translate(chrctrs)
                    cleaned = cleaned.translate(str.maketrans('', '', string.punctuation))
                    unspaced = ' '.join(cleaned.split())
                    output.write(unspaced + "\n")








