Secret_Word = "Zenless"

def check_req (userguess):
    length=len(userguess)
    if length == 1:
        return True
    else:
        return False

def check_alphabeth (userguess):
    if userguess.isalpha():
        return True
    else:
        return False
    
def check_answer(userguess, Secret_Word, num, usercorrectguess):
    if userguess == Secret_Word[num].lower():
        usercorrectguess.append(userguess)
        return True
    elif userguess == Secret_Word[num].upper():
        usercorrectguess.append(userguess)
        return True
    else:
        return False

def after_check(usercorrectguess):
    print("correct, guessed word so far:")
    for i in usercorrectguess:
        print(i)
    print("------------------------------")
        

def Main ():
    num = 0
    usercorrectguess= []
    while True:
        userguess = input("Guess the secret word: ")
        if check_alphabeth (userguess) is True:
            if check_req (userguess) is True:
                if check_answer(userguess, Secret_Word, num, usercorrectguess) is True:
                    num = num + 1
                    after_check(usercorrectguess)
                    if num == len(Secret_Word):
                        print ("The secret word is \"Zenless\"")
                        break
                elif check_answer(userguess, Secret_Word, num, usercorrectguess) is False:
                    print("Wrong, guess again")
            elif check_req (userguess) is False:
                print("Guess must be only a word")
        elif check_alphabeth (userguess) is False:
            print("Guess must be in alphabeth")


Main()



