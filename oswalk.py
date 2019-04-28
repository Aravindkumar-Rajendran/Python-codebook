'''oswalk function can be used to surf through the directory and files
By combining with filename match function, we can find the file dir if we know the filename 

Additionally, it enables our programs to 1. Seggrete by the filetype
                                         2. Counting the number of files of same filetype
                                         3. With  os function to organize our files
'''

import os
import fnmatch #filename match function library


#Counting the number of files based on filetype
def count(rootPath, pattern):
    count = 0
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            if filename:
                count +=1
    return count

def find_path(rootPath, pattern):
    filepaths = []
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            filepaths.append(os.path.join(root,filename))
    return filepaths


rootPath = "C:/Users"
pattern = "*.jpg" 
#pattern = ["*.png","*.jpg"] #we can use list to find many number of filetype

filePath = find_path(rootPath, pattern)
for files in filePath:
    print(files,end=", ")

c = count(rootPath, pattern)
print("%d"%c)
