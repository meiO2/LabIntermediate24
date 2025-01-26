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
    
def check_answer(userguess, Secret_Word, num):
    if userguess == Secret_Word[num].lower():
        return True
    elif userguess == Secret_Word[num].upper():
        return True
    else:
        return False 

def after_check(usercorrectguess):
    print("correct, guessed word so far:")
    for i in usercorrectguess:
        print (i)
    print("------------------------------")

def check2(userguess, usercorrectguess, num):
    if num >= 1:
        if userguess.upper() in usercorrectguess:
            return True
        elif userguess.lower() in usercorrectguess:
            return True
        else:
            return False
    else:
        return False

def Main ():
    num = 0
    usercorrectguess= []
    Health = 6
    while Health != 0:
        print ("Health:", Health)
        userguess = input("Guess the secret word: ")
        print("------------------------------")
        if check_alphabeth (userguess) is True:
            if check_req (userguess) is True:
                if check_answer(userguess, Secret_Word, num) is True:
                    usercorrectguess.append(userguess)
                    num = num + 1
                    after_check(usercorrectguess)
                    Health -= 1
                elif check_answer(userguess, Secret_Word, num) is False:
                    if check2(userguess, usercorrectguess, num) is True:
                        print ("You already guess this letter")
                        print("------------------------------")
                    elif check2(userguess, usercorrectguess, num) is False:
                        Health -= 1
                        print("Wrong, guess again")
                        print("------------------------------")
                if num == len(Secret_Word):
                    print ("The secret word is \"Car\"") 
                    break
            elif check_req (userguess) is False:
                print("Guess must be only a word")
        elif check_alphabeth (userguess) is False:
            print("Guess must be in alphabeth")
    else:
        print ("You ran out of health")


Main()