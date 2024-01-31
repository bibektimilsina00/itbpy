 
from login import login


history=[]








current_user= login("Ram")

# print(current_user)






def deposit(amount,current_user=current_user['name']):

    for index,user in enumerate( db_file.db):
         

        if user[index+1]["name"]==current_user:
            updated_amount= user[index+1]['balance']+amount
            user[index+1]['balance']=updated_amount
            history.append({
                current_user:f"Diposited: {amount}"
            }
 
            )
            
            
             

# while True:      
#     user_input=  input('enter')
#     if user_input=='1':
#         deposit(amount=2000)

#     if user_input.upper() == 'H':
#         print(history)
        








 
 
 





name = ''


name = 'hari'




