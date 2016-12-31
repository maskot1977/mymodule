import sys
import gzip
import time
import pyximport; pyximport.install(pyimport = True)
from mymodule import elapsed_time
from mymodule import elapsed_clock
from mymodule import comma_numeral

def birel_to_tabtable(file, outfile, transpose=False, symmetry=False, select='max', numtype='int'):
   start_time = time.time()
   start_clock = time.clock()
   matrix = {}
   cols = set([])
   rows = set([])
   f = open(outfile, 'w')
   for i, line in enumerate(gzip.open(file)):
      a = line.strip().split("\t")
      row = a[0]
      col = a[1]
      if transpose:
         col = a[0]
         row = a[1]
      rows.add(row)
      cols.add(col)
      if row not in matrix.keys():
         matrix.update({row:{}})
      if len(a) > 2:
         if numtype == 'int':
            if col not in matrix[row].keys():
               matrix[row][col] = int(a[2])
            if select == 'min':
               if matrix[row][col] > int(a[2]):
                  matrix[row][col] = int(a[2])
            else:
               if matrix[row][col] < int(a[2]):
                  matrix[row][col] = int(a[2])
         elif numtype == 'float':
            if col not in matrix[row].keys():
               matrix[row][col] = float(a[2])
            if select == 'min':
               if matrix[row][col] > float(a[2]):
                  matrix[row][col] = float(a[2])
            else:
               if matrix[row][col] < float(a[2]):
                  matrix[row][col] = float(a[2])
         else:
            matrix[row][col] = a[2]
      else:
         matrix[row][col] = 1
      if symmetry:
         tmp = col
         col = row
         row = tmp
         rows.add(row)
         cols.add(col)
         if row not in matrix.keys():
            matrix.update({row:{}})
         if len(a) > 2:
            matrix[row][col] = a[2]
         else:
            matrix[row][col] = 1

   for col in sorted(list(cols)):
      f.write("\t")
      f.write(col)
   f.write("\n")
   for row in sorted(list(rows)):
      f.write(row)
      for col in sorted(list(cols)):
         f.write("\t")
         if row in matrix.keys() and col in matrix[row].keys():
            f.write(str(matrix[row][col]))
         else:
            f.write("0")
      f.write("\n")
   f.close()
   elapsed_clock.elapsed_clock(start_clock)
   elapsed_time.elapsed_time(start_time)

if __name__ == '__main__':
   args = sys.argv
   file = args[1]
   outfile = args[2]
   birel_to_tabtable(file, outfile)
