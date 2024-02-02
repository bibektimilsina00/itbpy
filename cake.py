from datetime import datetime
import json
import os

data_file='db.json'
parsedData=[]
def write_data(cakes):
    with open(data_file, 'w') as file:
        for cake in cakes:


            parsedData.append(Cake.toJson(cake=cake))
        json.dump(parsedData, file, indent=4)

cakes=[]



class Cake():
    flavour:str
    shape:str
    size:int
    created_at:datetime=datetime.now()

    def __init__(self,flavour:str,shape:str,size:int=2) :

        
        self.flavour=flavour
        self.shape=shape
        self.size=size

    def toJson(cake):
        
        return {
            
        "flavour":cake.flavour,
        
        'shape':cake.shape,
        'size':cake.size,
            'created_at': str(cake.created_at)
        }



# choclate_cake:Cake=Cake("choclate","round",1)
# vanilla_cake:Cake= Cake("vanilla","square",2),
# strawberry_cake:Cake=Cake("strawberry","round",3),

# cakes=[choclate_cake,vanilla_cake,strawberry_cake]


# print(cakes[0].created_at)


while True:
    user_options= input("1: place order \n  2: dump daat else: view order")

    if(user_options =="1"):
        u_flavor,user_shape,user_size= input("Enter cake details:flavour, shape,size   ").split()


        cakes.append(
            Cake(flavour = u_flavor,shape =user_shape,size= int(user_size)  )
        )
    if(user_options == '2'):
        write_data(cakes=cakes)


    else:
        for index,cake in enumerate(cakes) :
            print(f"{index} cake\tflavour: {cake.flavour}\tshape:{cake.shape}\tsize:{cake.size},created_at:{cake.created_at}" )
            











