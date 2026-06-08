age = 19

if age >= 18:        # if deside on starting condition.
    print("you are an adult")
    print("you can vot") #(esme indentation lgate hai (indentation means sapace)jo colon k bad diya jata hai ,breases{} nhi)

print("thank you")



age = 16   # OUTPUT =  YOU ARE in school

if age >= 18:
    print("you are an adult")    # deside on starting condition
    print("you can vot")
elif age < 18 and age > 3:
    print("you are in school")   # starting condition true nhi hoi to ap dusri check kroo nhi to tisri krooo
else:
    print("you are a child")     # agr dono condition false hogi tp hm else m pahuchenge.


print("thank you")       #  yahan bs thank you print hoga q ki adult nhi hai   



age = 2  # OUTPUT =  YOU ARE A CHILD

if age >= 18:
    print("you are an adult")    
    print("you can vot")
elif age < 18 and age > 3:
    print("you are in school")  
else:
    print("you are a child")     


print("thank you")       



age = 19  # OUTPUT =  YOU ARE An AUDELT     YOU CAN VOT   THANK YOU.

if age >= 18:
    print("you are an adult")    
    print("you can vot")
elif age < 18 and age > 3:
    print("you are in school")  
else:
    print("you are a child")     


print("thank you")     




# RANGE

number = range(5)
print(number)