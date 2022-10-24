#Write a script that searches a folder you specify (as well as its subfolders, 
# up to two levels deep) and compiles a list of all .jpg files contained in there. 
# The list should include the complete path of each .jpg file.
#You should train: Using for loops, Using conditional statements,
#Working with pathlib, Thinking about nested loops
#If you are feeling bold, create a list containing each type of file extension you 
# find in the folder.

import pathlib        
desktop = pathlib.Path("/Users/xxx/Desktop/mainfolder_jpgmix").glob("**/*.jpg")
pathlist_alljpgs = []
for filepath in desktop:
    if filepath.suffix == ".jpg":
        pathlist_alljpgs.append(filepath)
print(pathlist_alljpgs)




        
