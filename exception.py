
a=input("Enter first number")
b=input("Enter Second number")
try:
    c=int(a)
    d=int(b)



    result= c/d

    
    print(result)




    
except ZeroDivisionError :
    print("You can't divide by zero")

except ValueError:
    print("you cant use int only ")

except:
    print("Some thing went wrong")

finally:
    print("This code will run any way")