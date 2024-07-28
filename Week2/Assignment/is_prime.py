# contains a function to check whether a number is a prime or not

def is_prime(number: int) ->bool:
    # a prime number can only be divided by 1 or by itself 

    if number <= 1:
        return False
    
    for x in range(2,number):
        if number%x == 0:
            return False
    
    return True    

# listing prime numbers: 1 3 5 7 11 13 17 23 31 