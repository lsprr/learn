import os
import shutil

path = 'F:\\Desktop\\Test2.txt'

try:
    # os.remove(path) # delete a file
    # os.rmdir(path) # delete an empty directory
    # shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print('The system cannot find ' + path)
except PermissionError:
    print('Access is denied')
except OSError:
    print('You cannot delete that using that function')
else:
    print(path + ' was deleted')
