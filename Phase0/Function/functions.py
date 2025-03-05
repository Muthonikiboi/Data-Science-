#Function Arguments
# def add_numbers(a,b ):
#     sum= a + b
#     print('The sum is:' ,sum)
# add_numbers(2,5)

##Arbitrary Arguments
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result +num
        print('Sum =', result)

find_sum(1, 2, 3)
find_sum(4, 19)