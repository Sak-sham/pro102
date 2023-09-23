import os
import shutil

fromdir='/Users/saksham/Downloads'
todir='/Users/saksham/Downloads/class102'

list_of_files=os.listdir(fromdir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=fromdir+'/'+file_name
        path2=todir+'/'+"imgs"
        path3=todir+'/'+"imgs"+'/'+file_name

        if os.path.exists(path2):
            print("We are moving the files..."+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("We are moving the files..."+file_name)
            shutil.move(path1,path3)