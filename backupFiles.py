import shutil
import os
source = input("Enter the file name : ")
destination = input("Enter file destination : ")
source = source+ '/'
destination = destination + "/"
list = os.listdir(source)
for i in list:
    shutil.copy((source + i ), destination)