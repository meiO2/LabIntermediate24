import random
Secret_Word = ["car", "cat", "run", "fly"]
score = 0

def hasil(userguess, correctguess, word):
    for x in range(len(word)):
        if userguess == word[x].lower():
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
        elif userguess == word[x].upper():
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
        elif userguess != word[x]:
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
    global score
    word = random.choice(Secret_Word)
    print ("Score:", score)
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
                if userguess in word.lower():
                    hasil(userguess, correctguess, word)
                    num = num + 1
                    print("tebakan benar:")
                    for i in correctguess:
                        print (i, end="")
                    print ("")
                    print("------------------------------")
                elif userguess in word.upper():
                    hasil(userguess, correctguess, word)
                    num = num + 1
                    for i in correctguess:
                        print (i, end="")
                    print("")
                    print("------------------------------")
                else:
                    if cek(userguess, correctguess, num) is False:
                        Health -= 1
                        print("Salah, tebak lagi")
                        print("------------------------------")
                if num == len(word):
                    score += 10
                    Secret_Word.remove (word)
                    print ("Congrats, kata rahasia adalah \"", word, "\"")
                    if len(Secret_Word) == 0:
                        print ("Game over, maximal score:", score)
                        return
                    else:    
                        num -= 3
                        print ("Score:", score)
                        print ("1. Continue")
                        print ("2. Quit")
                        pilih = input("Masukkan pilihan:")
                        if pilih == "1":
                            Main(Secret_Word)
                        elif pilih == "2":
                            print ("Game over, score:", score)
                            return
                        else:
                            break
                    break                
            else:
                print("Tebakan harus 1 huruf")
        else:
            print("Tebakan harus huruf")
    else:
        print ("GAME OVER")
        print ("Health Habis")

Main(Secret_Word)