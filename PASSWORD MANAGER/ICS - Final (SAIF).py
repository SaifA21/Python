# NAME - SAIF ABUOSBA 
# FILE NAME - ICS SUMMATIVE.py
# DATE - 2019 - 01 - 11
# DESCRIPTION - program allows user to store all of their passwords in a single program keeping them secure.
# In addition, it also allows users to check the strength of a desired password to keep them secure in an online world.
# If the user does not know how to create a good password, the program can create a user defined number of passwords at once. 

import time
import random

# TO ENCRYPT A PASSWORD THIS FUNCTION TAKES IN AN UNENCRYPTED PASSWORD AND APPENDS EACH CHARACTER IN A TEMP LIST
# IT THEN LOCATES THE CHARACTER INDEX IN ENCRYPT LIST, FROM THERE IT SWITCH'S IT WITH THE CHARACTER 2 INDEX'S AFTER
# NOTE THE RULE BELOW WAS CREATED FOR ADDED COMPLEXITY TO THE ENCRYPTION -  
# IF THE LOCATED INDEX IS SECOND TO LAST IN THE LIST, IT SWITCHES IT WITH THE FIRST INDEX AND IF ITS THE LAST  
# IT SWITCHES IT WITH 2ND INDEX OF THE LIST
# FROM THERE IT APPENDS EACH CHARACTER TO THE ENCYPY_PASS LIST AND JOINS IT TO CREATE A STRING PASSWORD WHICH IS RETURNED

def encrypt(pass_unencrypt):
    templist = []
    for x in(pass_unencrypt):
        templist.append(x)
    encrypt_pass = []
    for x in range(len(templist)):
        letter = templist[x]
        index = encryptList.index(letter)
        if index == 92:
            templist[x] = encryptList[0]
        elif index == 91:
            templist[x] = encryptList[1]
        else:
            templist[x] = encryptList[index+2]
        encrypt_pass.append(templist[x])
    stringEncrypt = "".join(encrypt_pass)
    return(stringEncrypt)# This is what gets stored so that it can be verified later

# THIS FUNCTION IS USED TO LOGIN TO THE PROGRAM, THE USER WILL HAVE 3 CHANCES TO ENTER THE PASSWORD CREATED DURING SETUP
# IF PASSWORD MATCHES THE ENCRYPTED LOGIN SAVED IN A TEXT FILE, THEY WILL PROCEED TO MAIN MENU
# IF NOT, AFTER 3 ATTEMPTS THE USER IS REDIRECTED TO THE FORGOT PASSWORD FUNCTION
# IF PASSWORD ENTERED MATCH'S DEFAULT, THEY WILL BE REDIRECTED TO THE NEW LOGIN FUNCTION 

def login():
    loginFile = open("encryptedLogin.txt","r")
    encryptLogin = loginFile.readline()# Stored encrypted login password, ">mSSx^(5" is default for "password"
    loginAttempt = 0
    print ("Welcome To Your Password Manager -")
    time.sleep(1)
    print ("If this is initial start up, enter “Pass1_” as default.")
    time.sleep(1)
    print("")
    while loginAttempt <3:
        login_pass = input("Please enter your password: ")
        check = encrypt(login_pass)
        loginAttempt += 1
        if check == encryptLogin:
            print("Password Confirmed...")
            time.sleep(2)
            print("")
            if encryptLogin == "|mSS#.": # If encryption match's the default, procced to new login
                newLogin()
            loginFile.close()
            mainMenu()
            break
        else:
            time.sleep(1)
            print ("Wrong Password")
            print ("")
            time.sleep(1)
    if loginAttempt == 3:
        print("You have attempted to login 3 times.")
        print("Redirecting to “forgot password” page.")
        time.sleep(2)
        forgotLogin(encryptLogin)


# THIS FUNCTION WILL ALLOW THE USER TO CREATE THEIR NEW PASSWORD FOR LOGIN IN TO THE PROGRAM
# THE PROGRAM WILL CHECK THE STRENGTH OF PASSWORD THEY ENTER UNTIL IT MATCHES THE CRITERIA
# WHEN A GOOD PASSWORD IS CHOSEN, THE PROGRAM ENCRYPTS THE PASSWORD AND SAVES IT IN A TEXT FILE
# THE USER THEN MUST ANSWER THE SECURITY QUESTION TO RETRIEVE THEIR FORGOTTEN PASSWORD IN THE FUTURE

def newLogin():
    print ("New Login - ")
    print("Since this is your first login, we ask that you change your password.")
    print("Your password must be at least 6 characters and contain at least 1 Uppercase, 1 lowercase, 1 number and 1 symbol/special character.")
    time.sleep(4)
    strength = False
    while strength != True:
        newLoginPass = input("Please enter a new password: ")
        strength = passStrength(newLoginPass)
        if strength == True:
            loginEncrypt = encrypt(newLoginPass)
            loginFile = open("encryptedLogin.txt","w")
            encryptLogin = loginFile.write(loginEncrypt)
            time.sleep(1)
            print("Password Approved")
            print("For added security, please answer the following question:")
            securityQuest = input("What is your favorite car make: ")
            securityEncrypt = encrypt(securityQuest)
            securityFile = open("securityQuest.txt","w")
            encryptAns = securityFile.write(securityEncrypt)
            print ("Your new login password is:", newLoginPass)
            print("You will now be directed to the main menu.")
            time.sleep(1)
        else:
            strength = False

# THE USER HAS 3 ATTEMPTS TO ENTER THEIR ANSWER TO THE SECURITY QUESTION TO RETRIEVE PASSWORD
# THE ANSWER IS ALSO ENCRYPTED AND CHECKED TO SEE IF IT MATCHES WITH THE SAVED ANSWER 
# AFTER 3 ATTEMPTS THEY ARE LOCKED OUT AND MUST RESTART THE PROGRAM

def forgotLogin(viewPass):
    securityFile = open("securityQuest.txt","r")
    encryptSecAnsEncrypted = securityFile.readline() # Stored encrypted answer to security question
    securityFile.close()
    print("Using the security question you answered previously, you will be able to retrive your login.")
    time.sleep(2)
    forgotCounter = 0
    while forgotCounter < 3:
        try:
            forgotAns = input("What is your favorite car make: ")
            securityEncryptCheck = encrypt(forgotAns)
            if securityEncryptCheck == encryptSecAnsEncrypted:
                check2 = decrypt(viewPass)
                print ("Your login Password is:",check2)
                print("You will now be redirected to the main menu.")
                time.sleep(2)
                mainMenu()
                break
        except:

            print("Incorrect")

            forgotCounter += 1

        if forgotCounter == 3:

            print("You have been locked out. Restart program to continue")
            


# THIS FUNCTION TAKES IN AN ENCRYPTED STRING AND DOES THE REVERSE OF THE ENCRYPT FUNCTION
# REFER TO ENCRYPT FUNCTION...

def decrypt(encryptedMessage):
    templist2 = []
    for y in(encryptedMessage):
        templist2.append(y)
    decryptList = []
    for z in range(len(templist2)):
        letter2 = templist2[z]
        index2 = encryptList.index(letter2)
        if index2 == 0:
            templist2[z] = encryptList[1]
        elif index2 == 91:
            templist2[z] = encryptList[92]
        else:
            templist2[z] = encryptList[index2-2]
        decryptList.append(templist2[z])
    stringDecrypt = "".join(decryptList)
    return(stringDecrypt)

# THIS FUNCTION TAKES IN A USER INPUT AND CHECKS IF IT MEETS THE CRITERIA SET
# CRITERIA: AT LEAST 1 CAP, 1 LOWER, 1 NUMBER, 1 SYMBOL AND AT LEAST 6 CHARACTERS
# IT CHECKS EACH CHARACTER AND ADDS A COUNT TO THE APPROPRIATE COUNTER
# IF CRITERIA IS MET, IT WILL RETURN TRUE, ELSE RETURN FALSE

def passStrength(strengthTBD):
    upperCount = 0
    lowerCount = 0
    numCount = 0
    symCount = 0
    length = 0
    for i in strengthTBD:
        if i in strengthUpper:
            upperCount += 1
        elif i in strengthLower:
            lowerCount += 1
        elif i in strengthNum:
            numCount += 1
        elif i in strengthSymbol:
            symCount += 1
        length += 1
    if upperCount >= 1 and lowerCount >= 1 and numCount >= 1 and symCount >= 1 and length >= 6:
        return True
    else:
        return False

# THE USER WILL MAKE A SELECTION FROM THE OPTIONS AND THEN WILL BE REDIRECTED AS REQUIRED 
def mainMenu():
    while True:
        try:
            print ("")
            print ("/"*78)
            print("Welcome to the Main Menu.")
            print ("1) Password Lookup")
            print ("2) Add Password")
            print ("3) Delete Password")
            print ("4) Generate Password")
            print ("5) Edit Password")
            print ("6) Check Password Strength")
            print ("7) Quit")

            mainMenuSelection = int(input("Choose one of the options above: "))
            if mainMenuSelection == 1:
                passLookup()
            if mainMenuSelection == 2:
                addPassMenu()
            if mainMenuSelection == 3:
                delPassMenu()
            if mainMenuSelection == 4:
                genPass()
            if mainMenuSelection == 5:
                editPassMenu()
            if mainMenuSelection == 6:
                strengthFunc ()
            if mainMenuSelection == 7:
                quitCheck = input("Are you sure you want to quit (Y/N): ")
                if quitCheck == "Y" or quitCheck == "y":
                    print("You have been signed out.")
                    time.sleep(2)
                    print("Goodbye")
                    break
                    
                else:
                    mainMenu()
                    break
        except:
            print("Error")
        
  

# THIS FUNCTION WILL ALLOW THE USER TO TEST THE STRENGTH OF THEIR DESIRED PASSWORD BEFORE USING IT
# IT WILL KEEP LOOPING UNTIL THEY CREATE A GOOD PASSWORD 
def strengthFunc():
    print("")
    print ("Welcome to the Check Password Strength Menu!")
    while True:
        try:
            checkPassMenu = input("Please enter the password you would like to check: ")
            result = passStrength (checkPassMenu)
            time.sleep(2)
            if result == True:
                print ("The password:", checkPassMenu,"is a good password.")
                goMain = input("Please press enter to go to main menu.")
                break
            else:
                print ("The password:", checkPassMenu,"is a weak password.")
                print ("Make sure the password contains at least 6 characters and contains",\
                       "at least 1 Uppercase, lowercase, number and 1 symbol/special character.")
                print ("")
        except:
            print("Error")

# THIS FUNCTION WILL ALLOW THE PROGRAM TO GENERATE STRONG PASSWORDS THAT CAN BE USED BY THE USER
# IT ASKS THE USER HOW MANY PASSWORDS THEY NEED AND CREATES 8 - CHARACTER PASSWORDS THAT ARE STRONG
# CHOOSING RANDOMLY FROM THE ENCRYPT LIST IS CREATES THE PASSWORDS AS IT APPENDS TO A LIST AND JOINS THEM INTO A STRING
def genPass():
    randPassList = []
    print("")
    print("Welcome to the genorate password menu!")
    time.sleep(2)
    numPass = int(input("Please enter the number of passwords you want to be genorated: "))
    valid = 0
    while valid != numPass:
        randPassMaker = []
        for m in range (8):
            choice = random.choice(encryptList)
            randPassMaker.append (choice)
        joinedPass = "".join(randPassMaker)
        validCheck = passStrength(joinedPass)
        if validCheck == True:
            randPassList.append(joinedPass)
            valid += 1
    print("These were the passwords genorated: ")
    for printGenorated in randPassList:
        time.sleep(1)
        print(printGenorated)
    goMain = input("Please press enter to go to main menu.")

# DEPENDING ON WHICH SELECTION THE USER CHOOSES, THE PROGRAM READS DATA FROM TEXT FILES ACCORDINGLY AND OUTPUTS THE NAME AND PASSWORD IN A NEAT FORMAT
def passLookup ():
    print ("")
    print ("Password Lookup Page - ")
    time.sleep (1)
    print("1) Passwords for Websites")
    print("2) Passwords for E-mails")
    print("3) Passwords for Banks")
    print("4) Miscellaneous Passwords")
    while True:
        try:
            ListSelectionView = int(input("Please choose one of the options above: "))
            if ListSelectionView == 1:
                lookUpFunc (cleanWebNameList,cleanWebPassList,choiceWeb)
                break

            elif ListSelectionView == 2:
                lookUpFunc (cleanEmailNameList,cleanEmailPassList,choiceEmail)
                break

            elif ListSelectionView == 3:
                lookUpFunc (cleanBankNameList,cleanBankPassList,choiceBank)
                break

            elif ListSelectionView == 4:
                lookUpFunc (cleanMisNameList,cleanMisPassList,choiceMis)
                break
            
            else:
                print("Not an option")
        except:
            print("Error")
    
# Takes in clean lists and displays the values  
def lookUpFunc (lookUpName, lookUpPass, lookUpChoice):
    print("")
    print ("Passwords For", lookUpChoice)
    time.sleep(1)
    for length in range(len(lookUpName)):
        print(lookUpName[length], ": ", lookUpPass[length])
    print("")
    returnMain = input("Please press enter to return to main menu. ")
    

# THIS FUNCTION ALLOWS USER TO ADD PASSWORDS TO DESGINATED TEXT FILES FOR FUTURE LOOK UP
# THE USER MAKES A SELECTON AND THEN ENTERS THE NAME OF WEBSITE, BANK, EMAIL ETC...
# IF THE NAME IS ALREADY FOUND, THUE USER WILL BE ASKED TO EDIT INSTED
# OTHERWISE, THE PASSWORD IS REQUESTED AND THEN IS ADDED TO THE FILE
def addPassMenu():
    while True:
        try:
            print("")
            print("Add Password Page -")
            time.sleep(1)
            print("1) Passwords for Websites")
            print("2) Passwords for E-mails")
            print("3) Passwords for Banks")
            print("4) Miscellaneous Passwords")
            listSelectionAdd = int(input("Please choose one of the options above: "))
            if listSelectionAdd == 1:
               addPass(cleanWebNameList,cleanWebPassList,webNameTxt,webPassTxt,choiceWeb)
               break
            
            elif listSelectionAdd == 2:
                addPass(cleanEmailNameList,cleanEmailPassList,emailNameTxt, emailPassTxt, choiceEmail)
                break
            
            elif listSelectionAdd == 3:
                addPass(cleanBankNameList,cleanBankPassList, bankNameTxt, bankPassTxt, choiceBank)
                break
            
            elif listSelectionAdd == 4:
                addPass(cleanMisNameList,cleanMisPassList, misNameTxt, misPassTxt, choiceMis)
                break
            
            else:
                print("Not an option")
        except:
            print("Error")

# Takes in the correct perameters to and gets user input to add passwords
# Overwrites existing text files after clearing them
def addPass(addName,addPass,nameFileAdd,passFileAdd, addChoice):
    print("")
    print("Passwords for",str(addChoice) + ": ")
    inputName = input("What is the name/link: ")
    if inputName in addName:
        print("Password for", inputName,"already saved, please edit password in main menu.")
        time.sleep(3)
    else:
        inputPass = input("What is the password: ")
        addName.append(inputName)
        addPass.append(inputPass)
        saveName = open(nameFileAdd,"w")
        for newName in addName:
            saveName.write(newName)
            saveName.write("\n")
        saveName.close()
        savePass = open(passFileAdd,"w")
        for newPass in addPass:
            savePass.write(newPass)
            savePass.write("\n")
        savePass.close()
        print("Password Saved!")
        print("Changes can be seen as of now.")
        time.sleep(2)
                

# Sends the correct perameters to the delPass function             
def delPassMenu ():
    while True:
        try:
            print("")
            print("Delete Password Page -")
            time.sleep(1)
            print("1) Passwords for Websites")
            print("2) Passwords for E-mails")
            print("3) Passwords for Banks")
            print("4) Miscellaneous Passwords")
            listSelectionDel = int(input("Please choose one of the options above: "))

            if listSelectionDel == 1:
                delPass (cleanWebNameList,cleanWebPassList,webNameTxt,webPassTxt,choiceWeb)
                break
            elif listSelectionDel == 2:
                delPass (cleanEmailNameList, cleanEmailPassList, emailNameTxt, emailPassTxt, choiceEmail)
                break
            elif listSelectionDel == 3:
                delPass (cleanBankNameList, cleanBankPassList, bankNameTxt, bankPassTxt, choiceBank)
                break
            elif listSelectionDel == 4:
                delPass (cleanMisNameList, cleanMisPassList, misNameTxt, misPassTxt, choiceMis)
                break
            else:
                print("Not an option")
        except:
            print("Error")


# This function takes in the appropriate peramters from the delPassMenu and removes
# the desired file. From there it overwrites the new lists
def delPass (delNames,delPasswords,delNameTxt,delPassTxt,delChoice):
    print("")
    print("Passwords for",str(delChoice) + ": ")
    inputNameDel = input("What is the name of the password that you want to delete: ")
    if inputNameDel in delNames:
        index = get_index(inputNameDel, delNames)
        del(delNames[index])
        del(delPasswords[index])
        clearDelName = open(delNameTxt,"w")
        clearDelName.write("")
        clearDelName.close
        clearDelPass = open(delPassTxt,"w")
        clearDelPass.write("")
        clearDelPass.close
        newNames = open(delNameTxt,"a")
        newPass = open(delPassTxt,"a")
        for numOfNameWrite in delNames:
            newNames.write(numOfNameWrite)
            newNames.write("\n")
        for numOfPassWrite in delPasswords:
            newPass.write(numOfPassWrite)
            newPass.write("\n")
        newNames.close()
        newPass.close()
        time.sleep(2)
        print("Password Has Been Removed")
        time.sleep(1)
    else:
        print("Password for", inputNameDel,"not found.")

# This will send perameters to the editPass function 
def editPassMenu():
    while True:
        try:
            print("")
            print("Edit Password Page -")
            time.sleep(1)
            print("1) Passwords for Websites")
            print("2) Passwords for E-mails")
            print("3) Passwords for Banks")
            print("4) Miscellaneous Passwords")
            listSelectionEdit = int(input("Please choose one of the options above: "))

            if listSelectionEdit == 1:
               editPass (webPassTxt, cleanWebNameList, cleanWebPassList, choiceWeb)
               break
            elif listSelectionEdit == 2:
                editPass (emailPassTxt, cleanEmailNameList, cleanEmailPassList, choiceEmail)
                break
            elif listSelectionEdit == 3:
                editPass (bankPassTxt, cleanBankNameList, cleanBankPassList, choiceBank)
                break
            elif listSelectionEdit == 4:
                editPass(misPassTxt,cleanMisNameList,cleanMisPassList, choiceMis)
                break
            else:
                print("Not an option")
        except:
            print ("Error")
            
# This function will take in the a pass txt file, a clean pass and name list and a string
# It will ask for the name of the password that needs to be changed and will find the index
# It replaces the password and writes it to the text file

def editPass (passTxt, nameValues, passValues, choice):
    print("")
    print("Passwords for",str(choice) + ": ")
    inputNameEdit = input("What is the name of the password that you want to edit: ")
    if inputNameEdit in nameValues:
        indexEdit = get_index(inputNameEdit, nameValues)
        newPass = input ("What is the new password: ")
        passValues[indexEdit] = newPass
        clearPassEdit = open(passTxt,"w")
        clearPassEdit.write("")
        clearPassEdit.close()
        newPassEdit = open(passTxt,"a")
        for savePass in passValues:
            newPassEdit.write(savePass)
            newPassEdit.write("\n")
        newPassEdit.close()
        time.sleep(2)
        print("Edit Saved!")
        time.sleep(1)
    else:
        print("Password for", inputNameEdit,"not found.")


# This function will find the index of a user input value and return the index
def get_index(indexName,nameList):
    while True:
        try:
            nameIndex = nameList.index (indexName)
            return nameIndex
            break
        except:
            print("An error occured.")

# This function cleans the variables holding txt file content, removing brackets, newlines and more.
# It returns the clean list
def clean (fileName):
    file = open(fileName,"r")
    fileValues = file.readlines()
    file.close()
    cleanList = []
    for value in fileValues:
        value = value.replace("[","").replace("]","").replace("'","").replace("\n","").replace(",","")
        cleanList.append(value)
    return cleanList



#Main

encryptList = ["Z","&","z","Q","q","&","*","r","R","(",\
               "s",")","S","A","1","a","#","m","N","$",\
               "p",":",">","q","?","Q",";","R","r","-",\
               "C","i","J","0","j","K","!","k","L","@",\
               "G","7","g","3","c","D","4","d","E","5",\
               "e","F","6","f","H","8","h","B","2","b",\
               "I","9","l","M","n","O","%","o","P","^",\
               "|","T","t","'","U","u","v","V","+","W",\
               "w","=","x","X","y","_","Y",".",",","~",\
               "<","{","}"]

strengthUpper = ["A","B","C","D","E","F","G","H","I",\
                 "J","K","L","M","N","O","P","Q","R",\
                 "S","T","U","V","W","X","Y","Z"]

strengthLower = ["a","b","c","d","e","f","g","h","i",\
                 "j","k","l","m","n","o","p","q","r",\
                 "s","t","u","v","w","x","y","z"]

strengthNum = ["0","1","2","3","4","5","6","7","8","9"]

strengthSymbol = ["?","@","_","-","#","$","%","^","&",\
                  "*","+","=","(",")","!","<",".","/",\
                  ":",";","{","}","|","[","]",",","~"]


webNameTxt= "websiteNames.txt"
webPassTxt = "websitePasswords.txt"
choiceWeb = "Websites"
cleanWebNameList = clean(webNameTxt)
cleanWebPassList = clean(webPassTxt)


emailNameTxt = "emailNames.txt"
emailPassTxt = "emailPasswords.txt"
choiceEmail = "Emails"
cleanEmailNameList = clean (emailNameTxt)
cleanEmailPassList = clean (emailPassTxt)


bankNameTxt = "bankNames.txt"
bankPassTxt = "bankPasswords.txt"
choiceBank = "Banks"
cleanBankNameList = clean(bankNameTxt)
cleanBankPassList = clean(bankPassTxt)


misNameTxt = "misNames.txt"
misPassTxt = "misPasswords.txt"
choiceMis = "Miscellaneous"
cleanMisNameList = clean(misNameTxt)
cleanMisPassList = clean(misPassTxt)

login()

