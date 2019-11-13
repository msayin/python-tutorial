print("Exponent Function Start from 2:41 minute")
print("Example1")
print(2**3)



print("Example2")
def raise_to_power (base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print (raise_to_power(3,4))