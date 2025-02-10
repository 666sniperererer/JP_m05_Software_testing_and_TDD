# Faktoriál
# n! = n * (n-1) * (n-2) * ... * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def fact(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError
    result = 1
    for i in range(2, n + 1):
        #print (f"i = {i}")
        result *= i
    return result

# Pomocí rekurze
# n! = n * (n-1)!
# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# 5! = 5 * 4!
# 4! = 4 * 3!
# ...
# 1! = 1 * 0! STOP
# 0! = 0 * (-1)! - toto už nedává smysl

def fact_r(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError
    if n == 0:
        return 1
    return n * fact_r(n-1)

if __name__ == '__main__':
    print(fact(5))
    print(fact_r(5))