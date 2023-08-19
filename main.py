

import os 
import shutil


print(os.getcwd())
#Changing current working directory to the one where the files will be download. 
#In this case I use my personal folder.
os.chdir(r'C:/Users/Admin/Downloads/File_Download/')     


#Getting the current path and change it to work with the download folder.
#The list will be by default sorted in download order. 
print(os.getcwd())                                    
list_downloads = os.listdir()  

#We want to move the files to an specific folder depending on their extensions.
#Using shutil module to move the files to the new folder. 
for file in list_downloads:
    if file[-4:] == '.jpg':
        shutil.move(file, r'C:/Users/Admin/Downloads/File_Download/Images')
        print(file)              
    elif file[-4:] == '.pdf' or file[-5:] == '.docx':
        shutil.move(file,r'C:/Users/Admin/Downloads/File_Download/Documents')
    elif file[-5:] == 'pptx' or file[-4:] == '.ppt':
        shutil.move(file, r'C:/Users/Admin/Downloads/File_Download/Presentations' )
    elif file[-4:] == 'mp4':
        shutil.move(file, r'C:/Users/Admin/Downloads/File_Download/Video')
    elif file[-4:] == '.zip':
        shutil.move(file, r'C:/Users/Admin/Downloads/File_Download/Rar')
    elif file[-5:] == '.xlsx' or file[-4:] == '.xls':
        shutil.move(file,r'C:/Users/Admin/Downloads/File_Download/Spreadsheet')

#If none of the files containes the former expressions, then the files will not 
#Change its directory. 
#Note: If the document already exist (or has the same name) it won't move the file
#And it will lead us to an error. 


#Automatically opens the directory if the user wish so. 
#Else, the program will shut down. 

check = input('Would you like to check the results? Yes/No ').lower()     

if check == 'yes': 
    os.startfile(r'C:/Users/Admin/Downloads/File_Download')
else:
    exit()
 




