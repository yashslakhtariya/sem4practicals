class YSL:
     @staticmethod
     def encrypt(txt, shift: int, out):
          ncrptd = ""
          with open(txt, 'r') as ysl:
               for char in ysl.read():
                    if char.isalpha():
                         if char.isupper():
                              ncrptd += chr((ord(char) + shift - 65) % 26 + 65)
                         else:
                              ncrptd += chr((ord(char) + shift - 97) % 26 + 97)
                    else:
                         ncrptd += char
               with open(out, 'w') as output:
                    output.write(ncrptd)
          

     @staticmethod
     def decrypt(txt, shift, out):
         YSL.encrypt(txt, -shift, out) 

file_in = input("Enter the filename to encrypt : ")
file_out = input("Enter the filename to write : ")
YSL.encrypt(file_in, 5, file_out)
