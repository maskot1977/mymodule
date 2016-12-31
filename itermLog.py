import sys
sys.path.append('/Users/kot/ipython_notebook/mymodule')
import os
import datetime
import removeControlCharacter

def itermLog(n):
    path = '/Users/kot/Documents/iTerm2_log/'
    files = os.listdir(path)
    
    files_with_time = []
    for file in files:
        stat = os.stat(path + file)
        last_modified = stat.st_mtime
        files_with_time.append([last_modified, file])

    #last_modified, file = reversed(files_with_time.sort())[n]
    #print ("%s   %s" % (dt.strftime("%Y-%m-%d %H:%M:%S"), file))
    index = 0
    for last_modified, file in reversed(files_with_time):
        index += 1
        if index == n:
            dt = datetime.datetime.fromtimestamp(last_modified)
            print ("%s   %s" % (dt.strftime("%Y-%m-%d %H:%M:%S"), file))
            f = open(path + file,"r")
            for row in f:
                print removeControlCharacter.removeControlCharacter(row)
                
            f.close()
            break
    
    if n == 0 or n == (index + 1):
        index = 0
        for last_modified, file in reversed(files_with_time):
            index += 1
            dt = datetime.datetime.fromtimestamp(last_modified)
            print ("%d    %s    %s" % (index, dt.strftime("%Y-%m-%d %H:%M:%S"), file))
    
if __name__ == '__main__':
    itermLog(1)