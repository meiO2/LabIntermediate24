Secret_Word = "car"

def hasil(userguess, correctguess):
    for x in range(len(Secret_Word)):
        if userguess == Secret_Word[x].lower():
            if x == 0:
                correctguess.pop(0)
                correctguess.insert(0, userguess)
                return correctguess
            elif x == 1:
                correctguess.pop(2)
                correctguess.insert(2, userguess)
                return correctguess
            elif x == 2:
                correctguess.pop(4)
                correctguess.insert(4, userguess)
                return correctguess
        elif userguess == Secret_Word[x].upper():
            if x == 0:
                correctguess.pop(0)
                correctguess.insert(0, userguess)
                return correctguess
            elif x == 1:
                correctguess.pop(2)
                correctguess.insert(2, userguess)
                return correctguess
            elif x == 2:
                correctguess.pop(4)
                correctguess.insert(4, userguess)
                return correctguess
        elif userguess != Secret_Word[x]:
            continue 

def cek(userguess, correctguess, num):
    if num >= 1:
        if userguess.upper() in correctguess:
            return True
        elif userguess.lower() in correctguess:
            return True
        else:
            return False
    else:
        return False

def Main (Secret_Word):
    num = 0
    correctguess= ["_"," ","_"," ","_"]
    Health = 6
    while Health != 0:
        print ("Health:", Health)
        userguess = input("tebak kata: ")
        print("------------------------------")
        if userguess.isalpha():
            if len(userguess)==1:
                if userguess in correctguess:
                        print ("huruf sudah ditebak, tebak lagi")
                        print("------------------------------")
                        continue
                if userguess in Secret_Word.lower():
                    hasil(userguess, correctguess)
                    num = num + 1
                    print("tebakan benar:")
                    for i in correctguess:
                        print (i, end="")
                    print ("")
                    print("------------------------------")
                    Health -= 1
                elif userguess in Secret_Word.upper():
                    hasil(userguess, correctguess)
                    num = num + 1
                    for i in correctguess:
                        print (i, end="")
                    print("")
                    print("------------------------------")
                    Health -= 1
                else:
                    if cek(userguess, correctguess, num) is False:
                        Health -= 1
                        print("Salah, tebak lagi")
                        print("------------------------------")
                if num == len(Secret_Word):
                    print ("Congrats, kata rahasia adalah \"Car\"") 
                    break
            else:
                print("Tebakan harus 1 huruf")
        else:
            print("Tebakan harus huruf")
    else:
        print ("GAME OVER")
        print ("Health Habis")

Main(Secret_Word)

