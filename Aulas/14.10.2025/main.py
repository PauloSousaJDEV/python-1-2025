def is_prime(num: int) -> bool:
    div = 2
    while num % div != 0:
        div = div + 1

    if div == num:
        return True
    else:
        return False