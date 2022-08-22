###############################
# FizzBuzz - Coding Challenge #
###############################

#FizzBuzz for loop to iterate over numbers
for x in range(0,101):
    #if divisible by 3 and 5 print FizzBuzz
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    #else if divisible by 3 print Fizz
    elif x % 3 == 0:
        print("Fizz")
    #else if divisible by 5 print Buzz
    elif x % 5 == 0:
        print("Buzz")
    #else print variable
    else:
        print(x)
