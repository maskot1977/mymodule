import sys
import time
import pyximport; pyximport.install(pyimport = True)

def elapsed_clock(start):
   etime = time.clock() - start
   if etime > (60 * 60 * 24):
      print (("elapsed_clock:\t{0}".format(etime / 60. / 60. / 24.)) + "[day]")
   elif etime > (60 * 60):
      print (("elapsed_clock:\t{0}".format(etime / 60. / 60.)) + "[h]")
   elif etime > 60:
      print (("elapsed_clock:\t{0}".format(etime / 60.)) + "[min]")
   else:
      print (("elapsed_clock:\t{0}".format(etime)) + "[sec]")

if __name__ == '__main__':
   elapsed_clock(time.clock())
