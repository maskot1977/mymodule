import sys
import gzip
import time
import pyximport; pyximport.install(pyimport = True)
from mymodule import elapsed_time
from mymodule import elapsed_clock
from mymodule import comma_numeral

def cat_gz(file, all=False, head=9):
   start_time = time.time()
   start_clock = time.clock()
   prev = ""
   num_of_columns = 0
   i = 0
   for i, line in enumerate(gzip.open(file)):
      if i == (head + 1):
         print ("... Omitted below ...\n")
         continue
      elif i > head:
         if all:
            continue
         else:
            break
      else:
         print line.strip()
         if num_of_columns != len(line.split("\t")):
            num_of_columns = len(line.split("\t"))
            print ("Num of columns in line {1}:\t{0}".format(num_of_columns, i))
         else:
            num_of_columns = len(line.split("\t"))
         if line == prev:
            sys.stderr.write("Same sentence appears more than once at line {0}.\n".format(i))
         prev = line
   print ("*===== Summary =====*")
   print ("Num of columns:\t{0}".format(comma_numeral.comma_numeral(num_of_columns)))
   if all:
      print ("Num of rows:\t{0}".format(comma_numeral.comma_numeral(i)))
   else:
      sys.stderr.write('If you want to know num of rows, specify the parameter "all=True"\n')
   elapsed_clock.elapsed_clock(start_clock)
   elapsed_time.elapsed_time(start_time)

if __name__ == '__main__':
   args = sys.argv
   file = args[1]
   cat_gz(file)
