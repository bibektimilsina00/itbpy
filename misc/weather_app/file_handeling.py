import os

try:
    file=open('my_file.txt','r')

    text= file.readlines(10)
    print(text)

    

except:
    print("some thing went worong!!")

finally:
    print('Done !')