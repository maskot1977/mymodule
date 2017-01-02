import sys
import gzip
import time
if __name__ != '__main__':
   import pyximport; pyximport.install(pyimport = True)
sys.path.append(".")
from mymodule import elapsed_time
from mymodule import elapsed_clock
from mymodule import comma_numeral

def remove_col(file, outfile, remove_cols):
   start_time = time.time()
   start_clock = time.clock()
   if type(remove_cols) != list:
      sys.stderr.write('parameter must be a list')
      return
   if file == outfile:
      sys.stderr.write('Two files must not be the same.')
      return
   f = open(outfile, 'w')
   if outfile[-3:] == '.gz':
      f.close()
      f = gzip.open(outfile, 'w')
   i = 0
   cols = []
   #print remove_cols
   for i, line in enumerate(gzip.open(file)):
      if i == 0:
         cols = line.replace("\n", "").split("\t")
      a = line.replace("\n", "").split("\t")
      b = [x for x, y in zip(a, cols) if y not in remove_cols]
      #print b
      line2 = "\t".join(b)
      f.write(line2)
      f.write("\n")
   f.close()
   elapsed_clock.elapsed_clock(start_clock)
   elapsed_time.elapsed_time(start_time)

if __name__ == '__main__':
   args = sys.argv
   file = args[1]
   outfile = args[2]
   remove_cols = args[3:]
   print remove_cols
   remove_col(file, outfile, remove_cols)
