import gzip
import sys
import time
import pyximport; pyximport.install(pyimport = True)
from mymodule import get_col_name_frm_gz
from mymodule import get_row_name_frm_gz
from mymodule import elapsed_time
from mymodule import elapsed_clock

def compare_tabtables(files):
  start_time = time.time()
  start_clock = time.clock()
  if type(files) != list:
    sys.stderr.write('parameter must be a list')
    return
  cols = []
  rows = []
  for file in files:
    cols.append(get_col_name_frm_gz(file))
    rows.append(get_row_name_frm_gz(file))

  print "*===== Compare cols =====*\n"
  for col1, file1 in zip(cols, files):
    print ("{0} :\n{1} cols, {2} uniq cols".format(file1, len(col1), len(set(col1))))
    print col1[:4]
    for col2, file2 in zip(cols, files):
      if file1 == file2:
        continue
      sa1 = len(set(col1) - set(col2))
      sa2 = len(set(col2) - set(col1))
      seki = len(set(col1) & set(col2))
      if sa1 == 0 and sa2 == 0:
        print ("  against {0} : Same".format(file2))
      elif seki == 0:
        print ("  against {0} : No common".format(file2))
      else:
        print ("  against {0} : ".format(file2))
        print ("         {0} common cols, {1} uniq cols".format(seki, sa1))
    print

  print "*===== Compare rows =====*\n"
  for row1, file1 in zip(rows, files):
    print ("{0} :\n{1} rows, {2} uniq rows".format(file1, len(row1), len(set(row1))))
    print row1[:4]
    for row2, file2 in zip(rows, files):
      if file1 == file2:
        continue
      sa1 = len(set(row1) - set(row2))
      sa2 = len(set(row2) - set(row1))
      seki = len(set(row1) & set(row2))
      if sa1 == 0 and sa2 == 0:
        print ("  against {0} : Same".format(file2))
      elif seki == 0:
        print ("  against {0} : No common".format(file2))
      else:
        print ("  against {0} : ".format(file2))
        print ("         {0} common rows, {1} uniq rows".format(seki, sa1))
    print

  print "*===== Compare cols and rows =====*\n"
  for col1, file1 in zip(cols, files):
    print ("{0} :\n{1} cols, {2} uniq cols".format(file1, len(col1), len(set(col1))))
    for row2, file2 in zip(rows, files):
      print ("   {0} :\n   {1} rows, {2} uniq rows".format(file2, len(row2), len(set(row2))))
      sa1 = len(set(col1) - set(row2))
      sa2 = len(set(row2) - set(col1))
      seki = len(set(col1) & set(row2))
      if sa1 == 0 and sa2 == 0:
        print ("      Same".format(file2))
      elif seki == 0:
        print ("      No common".format(file2))
      else:
        print ("      {0} common items, {1} uniq items".format(seki, sa1))
    print

  elapsed_clock.elapsed_clock(start_clock)
  elapsed_time.elapsed_time(start_time)
  return #(cols, rows)

if __name__ == '__main__':
   args = sys.argv
   compare_tabtables(args[1:])
