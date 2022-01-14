import os 
import shutil
path = '/Users/sandh/Documents'
print('before copy msg')
print(os.listdir(path))
source = '/Users/sandh/Downloads/12-Chemistry-Ncert-Chapter-3.pdf'
destination = '/Users/sandh/Documents/spring1.pdf'
dest = shutil.copy(source,destination)
print('after copy msg')
print(os.listdir(path))