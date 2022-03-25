import shutil 
import os
import datetime
import time
path = "C:/Users/sandh/python/class103Project/"
print(os.stat(path).st_ctime)
time = time.ctime(os.stat(path).st_ctime)
print(time)
