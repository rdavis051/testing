###########################
# This is the creation of
# the factorial program.
###########################

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

n = 5
x = factorial(n)
print(x)

