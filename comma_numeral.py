import sys
import pyximport; pyximport.install(pyimport = True)

def comma_numeral(num = 1234567890):
   num = str(num)
   ret = ""
   for c in reversed(num):
      if len(ret)%4 == 3:
        if len(ret) > 0:
          ret = ',' + ret
      ret = c + ret
   return ret

if __name__ == '__main__':
   args = sys.argv
   if len(args) > 1:
      print comma_numeral(args[1])
   else:
      print comma_numeral()
