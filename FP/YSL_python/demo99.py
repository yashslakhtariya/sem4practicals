while True:
     mala = input("\nEnter number of rounds you chant : ")
     
     if mala.__contains__("quit") or mala.__contains__("exit"):
          break
     
     try:
          mala = int(mala)
          if mala < 16:
               print("\n\tYou are not chanting atleast 16 rounds of Hare Krishna Mahamantra\n\tNobody can save you now!!! Hare Krishna !!!")
          
     except Exception as err:
          # print(err)
          print("\n\tPlease enter a valid number of rounds!")
     
     else:
          if mala >= 16:
               print(f"\n\tHaribol!!! You are chanting {mala} rounds daily!\n\tJay Prabhupada!")
          
     finally:
          print("\n\tHare Krishna!")
