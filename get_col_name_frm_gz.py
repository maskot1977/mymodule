import gzip
import sys

def get_col_name_frm_gz(file, head=10):
   ret = []
   for i, line in enumerate(gzip.open(file)):
      ret = line.strip().split("\t")
   return ret

if __name__ == '__main__':
   args = sys.argv
   file = args[1]
   get_col_name_frm_gz(file)
