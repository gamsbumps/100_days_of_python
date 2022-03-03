def prime_checker(number):
    prime_number = True
    for num in range(2, number):
        if number % num == 0:
            prime_number = False
    if prime_number:
        print(f'{number} is a prime number.')   
    else:
        print(f'{number} is not a prime number.')    


n = int(input("Check this number: "))
prime_checker(number=n)


