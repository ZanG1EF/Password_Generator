import random #Adding the required module to make randomization

char = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","J","j","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","S","s","T","t","y","Y","u","U","v","V","w","W","x","X","z","Z","0","1","2","3","4","5","6","7","8","9","*","$","µ","£","%","ù","+","é","è","?","!","=","^","<",">","&","-","_","{","}","(",")","à","ç","|","~","[","]","/","§","°","|"]
#This is the list that contain every characters that will be used for the password

randomchar1 = random.choice(char)
randomchar2 = random.choice(char)
randomchar3 = random.choice(char)
randomchar4 = random.choice(char)
randomchar5 = random.choice(char)
randomchar6 = random.choice(char)
randomchar7 = random.choice(char)
randomchar8 = random.choice(char)
randomchar9 = random.choice(char)
randomchar10 = random.choice(char)
#The 10 variables above are the chosen characters from the previous list


while True:
    choice = input("Type G to generate a Password, Q to quit : ") 
    #Input that asks to the user if he wants to generate a pswd or to quit  
    if choice == "G" or choice == "g":
        pswd = randomchar1 + randomchar3 + randomchar4 + randomchar5 + randomchar6 + randomchar7 + randomchar8 + randomchar2 + randomchar9 + randomchar10 
        #Creation of the variable that will combine the 10 characters
        print ("The Generate Password is : ", pswd)
        #Print of the generated password
        break
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Incorrect Option !")
        #Error management



