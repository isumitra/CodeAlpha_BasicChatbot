name = "sumitra" 

print(name.upper())  # output = SUMITRA
print(name.lower())  # output = sumitra


# find a character ....

name = "sumitra Singh"
print(name.find('s')) # ye 0 se suru hota hai ,agar yhan vo characater h to ye uski position  ko print krega 
# agar nhi hai to ye -1 print krega.

name = "sumitra Singh"
print(name.find('singh'))  # output = -1 because small singh not exist.

# next operations...
# string k andar kisi v part ko utha skte hai aur use kisi aur part se replace kr skte hai.

name = "sumitra rathore"
print(name.replace("sumitra rathore", "baby singh"))  # output = baby singh

# then,

name = "sumitra rathore"
print(name.replace("rathore","singh"))  # output = sumitra singh

# replace  character

name = "sumitra rathore"
print(name.replace("s","h"))  # output = humitra rathore 

# check the , how to exist substring or character.. ye nhi dekhna ki index kya hai
# using in() function

# kya captial s ek character hai jo hmare name string k andar exist krta hai ..... print= true

name = "Sumitra rathore"
print('S' in name)  # output = true.
print('p' in name)  # output = false. because p are no exist in string name.
print('rathore' in name)  # output = true.
print('singh' in name)