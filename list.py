#  LIST   (collection of items  , it is complex datatype ,[] used this )


marks = [95,98, 97]
print(marks)          # 95, 98, 97

marks = [95,98, 97]
print(marks[1])       #  98

marks = [95,98, 97]
print(marks[0])       # 95


marks = [95,98, 97]     
print(marks[-1])       #  97

marks = [95,98, 97]
print(marks[-2])      #  98


marks = [95,98, 97]
print(marks[1:2])   #[98]


marks = [95,98, 97]
print(marks[0:2])   #[95,98]


marks = [95,98, 97]
print(marks[1:3])      #[98,97]

# using loop 

marks = [95,98, 97]

for score in marks:
    print(score)

    #  APPEND OPERATION

marks = [95,98, 97]

marks.append(99)
print(marks)        # [95,98,97,99]

     #  INSERT  OPERATION

marks = [95,98, 97]
marks.insert(0,99)
print(marks)