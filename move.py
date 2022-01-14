import os 
import shutil
path = '/Users/sandh/Documents'
print('before copy msg')
print(os.listdir(path))
source = '/Users/sandh/Downloads/testFile.txt'
destination = '/Users/sandh/Documents/testFile2.txt'
dest = shutil.move(source,destination)
print('after copy msg')
print(os.listdir(path))