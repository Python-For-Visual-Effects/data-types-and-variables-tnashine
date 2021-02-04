"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)


# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
x = 64
y = 32
print(x+y)


# 3.- Make a program that prints a sentence that includes at least 3 variables.
student = "Tanvi Nashine"
subject = "Python"
college = "Seneca college"
print(
    "Hello, my name is " + student + ", and I "
    " am your " + subject + " student at " + college
)




# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
a = "Python program"
print("This is my first " + str(a))
print(len("This is my first" + a))




# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
x = 1920*1.1
y = 1080*1.1
print("The 10% overscan of 1920 is ", x , ", the value of 1080 is ", y)
