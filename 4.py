largest_palindrome = 0

for first_num in range(100,1000):
    for second_num in range(100,1000):
        product = first_num*second_num
        if str(product) == str(product)[::-1]:
            if product > largest_palindrome:
                largest_palindrome = product
            


print largest_palindrome
