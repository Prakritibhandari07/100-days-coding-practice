applePrice=250
budget=260
if(applePrice<budget):
    print("Alexa,add 1 kg apples to the cart.")
else:
    print("Alexa,do not buy apple to the cart.")

num=int(input("Enter the value of num: "))
if(num<0):
    print("Number is negative.")
elif(num==0):   
    print("Number is zero.")
elif(num==999):    
   print("Number is special.")
else:
   print("Number is positive.")

num=16
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("Number is between (0-10).")
    elif(num>10&num<=20):        
        print("Number is between (11-20).")
    else:
        print("Number is greater than 20.")
else:
    print("Number is zero.")        