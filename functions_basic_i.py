#1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

# # Prediction: will return 5.


#2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Prediction: will return 5. 

# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

# Prediction: will return 5, 10. Returned only 5 because will exit the code block after the first return statement.

# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

# Prediction:  Will return 5.


# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

# Prediction:  Will print 5. Printed out 5, None. Printed out none because the function did not "return" anything. 


# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# Prediction:  Will print out 8.  Printed out 3, 5.


# #7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))

# Prediction:  Will not print out anything since the function does not do anything before the return statement.  Printed out 25.


# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())

# Prediction:  Will return 100, 10.


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) #Will return 7.
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #Will return 14.
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #Will return 714. Returned 21.


# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5)) #Prediction:  Will return 8.


# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

#Prediction: Will print out 500, 300, 500, 300, 500.  Printed out 500,500,300,500.


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)

# Prediction: Will print out 500,300,500,300,500. Printed out 500,500,300,500.


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)
#Prediction:  Will print out 500,500,300. Printed 500,500,300,300.

# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()
#Prediction: Will print 1, 2.  Printed 1,3,2.


# #15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)
#Prediction: Will print 1, 3, 5, 10, 1, 3, 5, 10. Printed 1,3,5,10.