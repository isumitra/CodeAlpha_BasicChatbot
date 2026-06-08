 # An arthmatis operations are special symbol used to perform mathematical operations on number in python.
# + ,-, * , / , % , ** ,//

print(5 + 2)  # OUTPUT = 7
print(5 - 2)  # OUTPUT = 3
print(5 * 2)  # OUTPUT = 10
print(5 / 2)  #OUTPUT = 2.5
print(5 // 2)  #OUTPUT = 2
print(5 % 2)   #OUTPUT = 1   esko moduler ,or remender operator v kehete hai.
print(5 ** 2)  # OUTPUT = 25   esko power operator v kehete hai. 

# shortcut in calculation.

i = 5
i = i = 2
i += 2

i -= 2

i *= 2


# OPERATOR PRECEDENCE

result = 2 + 3 * 5 
print(result)  # OUTPUT = 17

result = (2 + 3) * 5
print(result)            # 25

result = 2 + 3 / 5
print(result)          #  2.6 



   #  COMPAESION OPERATOR  esme jo op-erations hote hai vo boolean value return krte hai   true or false.

print(3>2)  # true
print(3<2)  # false
print(3<=2)  # false
print(3>=2)  # true
print(3 == 2)  # false
print(3 == 3)  # true
print(3 != 3)  # false
print(3 != 2)  # true  


# LOGICAL OPERATORS 


# there are three types of operators in python
# 1.  or operator  ,( if atlist one is true    to print true hoga   nhi to dono false hoga tv print hoga false.)

print(2 > 3 or 2 > 1)     #true

# 2. AND OPERATOR    (dono condition true hogi tv true print krega   nhi to false.)

print(3 > 2 and 8 > 6)    #true
print(3 > 4 and 3 > 2)    #false


# 3. NOT OPERATOR   (  ye true ko false bna deta hai , aur false ko true bna deta hai.)
print(not 5 > 4)   #false  (ye true ko false kr diya hai)
print(not 5 > 7)    # true   (esne false ko true kr diya hai)