from YSL_io import *
class YSL:
     @staticmethod
     def fileread(filename):
          with open(filename, 'r') as ysl:
               ch = 0
               wrd = 0
               ln = 0
               for line in ysl:
                    ln += 1
                    words = line.split(' ')
                    wrd += len(words)
                    ch += len(line)
               printORNG(f"Number of characters : {ch}")
               printBLU(f"Number of words : {wrd}")
               printMGNTA(f"Number of lines : {ln}")


f = inputGRN("Enter the filename to read : ")
YSL.fileread(f)
