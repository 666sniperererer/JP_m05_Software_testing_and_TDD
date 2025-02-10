# Definujte funkci is_prime(n), která vrací True, pokud je zadané číslo prvočíslem

def is_prime(n):
    # TODO: použitý algoritmus není optimální, zkuste jej vylepšit
    if n < 2:
        return False
    for i in range (2, n):
        #if n / i == n // i:
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in range(500):
        if is_prime(i):
            print(f"{i} je prvočíslo")
        else:
            print(f"{i} není prvočíslo")