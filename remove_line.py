import sys
import gzip
import time
if __name__ != '__main__':
   import pyximport; pyximport.install(pyimport = True)
sys.path.append(".")
from mymodule import elapsed_time
from mymodule import elapsed_clock
from mymodule import comma_numeral

def remove_line(file, outfile, lines):
   start_time = time.time()
   start_clock = time.clock()
   if type(lines) != list:
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
   lines = [int(x) for x in lines]
   for i, line in enumerate(gzip.open(file)):
      if i in lines:
         continue
      else:
         f.write(line)
   f.close()
   elapsed_clock.elapsed_clock(start_clock)
   elapsed_time.elapsed_time(start_time)

if __name__ == '__main__':
   args = sys.argv
   file = args[1]
   outfile = args[2]
   lines = args[3:]
   print lines
   remove_line(file, outfile, lines)
