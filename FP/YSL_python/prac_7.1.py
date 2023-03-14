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
               print(f"Number of characters : {ch}")
               print(f"Number of words : {wrd}")
               print(f"Number of lines : {ln}")


f = input("Enter the filename to read : ")
YSL.fileread(f)
