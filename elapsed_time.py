import time
import pyximport; pyximport.install(pyimport = True)

def elapsed_time(start):
   etime = time.time() - start
   if etime > (60 * 60 * 24):
      print (("elapsed_time:\t{0}".format(etime / 60. / 60. / 24.)) + "[day]")
   elif etime > (60 * 60):
      print (("elapsed_time:\t{0}".format(etime / 60. / 60.)) + "[h]")
   elif etime > 60:
      print (("elapsed_time:\t{0}".format(etime / 60.)) + "[min]")
   else:
      print (("elapsed_time:\t{0}".format(etime)) + "[sec]")
   print (str(time.ctime()))

if __name__ == '__main__':
   elapsed_time(time.time())
