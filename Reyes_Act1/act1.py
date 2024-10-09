name = input("Enter your name: ") 



celsius =  5/9 
fahrenheit = 9/5

print("Choose your type of conversion: ")
print("1. Celsius to Fahrenheit")
print ("2. Fahrenheit to Celsius")


a = int(input("Enter 1 or 2:"))


if a == 1 :
    b = float(input("Enter Temperature in Celsius: "))
    Temp1 = b * fahrenheit - 32
    print (f"Hello,"+ name +"! "+ str(b) +" celsius"+"is equal to "+ str(Temp1)+" Fahrenheit") 
    
elif a == 2 :
    c = float(input("Enter Temperature in Fahrenheit: "))
    Temp2 =  c * celsius + 32 
    print (f"Hello,"+ name +"! "+ str(c) + " Fahrenheit "+"is equal to "+ str(Temp2) + " celsius")
    
else:
    print ("Syntax Error")
    
    
    
  