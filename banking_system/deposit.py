
from db_file import db




def deposit(amount,current_user ):

    for index,user in enumerate(db):
         

        if user[index+1]["name"]==current_user:
            from main import history
            updated_amount= user[index+1]['balance']+amount
            user[index+1]['balance']=updated_amount
            history.append({
                current_user:f"Diposited: {amount}"
            }
 
            )
            