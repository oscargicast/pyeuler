def sum_prime_numbers(limit):
    summatory = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            summatory = summatory + num
    return summatory


print(sum_prime_numbers(1000))
