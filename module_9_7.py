def is_prime(f):
    def wraper(*args, **kwargs):
        result = f(*args, **kwargs)
        for i in range(2, result):
            if not result % i:
                is_prime_out = "Составное"
                break
        else:
            is_prime_out = "Простое"
        print(is_prime_out)
        return result

    return wraper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

# Простое
# 11
