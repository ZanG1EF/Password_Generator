import random

char = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","J","j","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","S","s","T","t","y","Y","u","U","v","V","w","W","x","X","z","Z","0","1","2","3","4","5","6","7","8","9","*","$","µ","£","%","ù","+","é","è","?","!","=","^","<",">","&","-","_","{","}","(",")","à","ç","|","~","[","]","/","§","°","|"]
#This is the list that contains every character that will be used for the password

while True:
    choice = input("Type G to generate a Password, Q to quit : ") 
    #Input that asks the user if they want to generate a password or quit  
    if choice == "G" or choice == "g":
        pswd = ""
        for i in range(10):
            pswd += random.choice(char) 
            #append a random character to the password
        print ("The Generated Password is: ", pswd)
        #Print of the generated password
        break
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Incorrect Option !")
        #Error management
