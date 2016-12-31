import gzip
import sys
import pyximport; pyximport.install(pyimport = True)

def get_row_name_frm_gz(file, head=10):
   ret = []
   for i, line in enumerate(gzip.open(file)):
      ret.append(line.split("\t")[0])
   return ret

if __name__ == '__main__':
   args = sys.argv
   file = args[1]
   print get_row_name_frm_gz(file)
