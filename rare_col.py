import gzip
import sys
import time
import pyximport; pyximport.install(pyimport = True)
#sys.path.append(".")
from mymodule import get_col_name_frm_gz
from mymodule import get_row_name_frm_gz
from mymodule import elapsed_time
from mymodule import elapsed_clock
import numpy as np

def rare_col(files, minval=2):
  start_time = time.time()
  start_clock = time.clock()
  if type(files) != list:
    sys.stderr.write('parameter must be a list')
    return
  cols = []
  freqs = np.array([])
  for file in files:
    for i, line in enumerate(gzip.open(file)):
      if i == 0:
        a = line.replace("\n", "").split("\t")[1:]
        if len(cols) == 0:
          cols = a
        if cols != a:
          sys.stderr.write('columns must be the same.')
          return
      else:
        a = np.array([1 if float(v) > 0 else 0 for v in line.replace("\n", "").split("\t")[1:]])
        if len(freqs) == 0:
          freqs = a
        else:
          freqs += a
    
  elapsed_clock.elapsed_clock(start_clock)
  elapsed_time.elapsed_time(start_time)
  return [x for x, y in zip(cols, freqs) if y < minval]

if __name__ == '__main__':
   args = sys.argv
   print rare_col(args[1:])
