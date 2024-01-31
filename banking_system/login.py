from db_file import db





def login(name):
    for index,user in enumerate(db):
        if user['name']==name:
            print(user)
        # if name==user['name']:
        #  print(user['name'])
        # if user[index+1]["name"]==name:
        #     return user[index+1]



