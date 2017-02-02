import sys
import gzip
import time
import pyximport; pyximport.install(pyimport = True)
from mymodule import elapsed_time
from mymodule import elapsed_clock
from mymodule import comma_numeral

def tabtable_to_birel(file, outfile, transpose=False, symmetry=False, select='max', numtype='int'):
   start_time = time.time()
   start_clock = time.clock()
   f = open(outfile, 'w')
   if outfile[-3:] == '.gz':
      f.close()
      f = gzip.open(outfile, 'w')
   col = []
   for i, line in enumerate(gzip.open(file)):
     if i == 0:
       col = line.replace("\n", "").split("\t")
     else:
       a = line.replace("\n", "").split("\t")
       for c, v in zip(col[1:], a[1:]):
         if float(v) != 0:
           f.write(a[0])
           f.write("\t")
           f.write(c)
           f.write("\t")
           f.write(v)
           f.write("\n")
   f.close()
   elapsed_clock.elapsed_clock(start_clock)
   elapsed_time.elapsed_time(start_time)

if __name__ == '__main__':
   args = sys.argv
   file = args[1]
   outfile = args[2]
   tabtable_to_birel(file, outfile)
