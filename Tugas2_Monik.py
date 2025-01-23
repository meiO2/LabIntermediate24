Secret_Word = "Car"

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
    
def check2(userguess, usercorrectguess):
    for i in usercorrectguess:
        if userguess == i:
            return True
        else:
            return False

def after_check(usercorrectguess, Secret_Word):
    print("correct, guessed word so far:")
    for i in usercorrectguess:
        print (i)
    print("------------------------------")
        
def HP(usercorrectguess, userguess):
    Health = 6
    for x in range (0,7):
        if check2(userguess, usercorrectguess) is False:
            Health -= 1
            print ("Health:", Health)
        else:
            break

def Main ():
    num = 0
    usercorrectguess= []
    print ("Health: 6")
    while True:
        userguess = input("Guess the secret word: ")
        if check_alphabeth (userguess) is True:
            if check_req (userguess) is True:
                if check_answer(userguess, Secret_Word, num, usercorrectguess) is True:
                    num = num + 1
                    after_check(usercorrectguess, Secret_Word)
                    HP(usercorrectguess, userguess)
                    if num == len(Secret_Word):
                        print ("The secret word is \"Car\"")
                        break
                elif check_answer(userguess, Secret_Word, num, usercorrectguess) is False:
                    print("Wrong, guess again")
            elif check_req (userguess) is False:
                print("Guess must be only a word")
        elif check_alphabeth (userguess) is False:
            print("Guess must be in alphabeth")


Main()