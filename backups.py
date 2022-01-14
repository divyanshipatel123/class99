import os
#print(os.system('date'))
#os.mkdir('./testFile')
#print(os.getcwd())
#path = "/Users/sandh/python/testFile/"
isExist = os.path.exists('/Users/sandh/OneDrive/Desktop')
print(isExist)
path = "backups.py"
routeTxt = os.path.splitext(path)
#print('file name : ',routeTxt[0])
#print('file extension: ',routeTxt[1])
