print("Welcome to Kabhre Central Bank!!\n")

dictt={
    1:{"name":"Rahul Zain","address":"Banepa","balance":250000,"history":[]},
    2:{"name":"Laxman Padey","address":"Khopase","balance":300000,"history":[]},
    3:{"name":"Pemba Tmg","address":"Dhulikhel","balance":275000,"history":[]},
    4:{"name":"Nishan Prasai","address":"Sankhu","balance":400000,"history":[]}
}
def login(name):
    userExist=False
 
    user_input=input("Enter your name: ")
    for i in dictt:
        a=dictt[i]['name']
        if(user_input==a):
            userExist=True
           
             
            break
         

       
         
         
         
    if(      userExist   ):
        for i in dictt:
            a=dictt[i]['name']
        
            if(user_input==a):
                    print("Successfully logged in!")
                    print(dictt[i])
          
    else:
                print("Invalid username!")

 
login("Rahul Zain")