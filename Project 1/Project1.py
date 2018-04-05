# CS 2221 Project 1
# Joseph Petitti
# 8 November 2017
import time


def euclid(m, n):
    # Input: Two positive integers m and n
    # Output: Greatest common divisor of m and n
    while n != 0:
        r = m % n
        m = n
        n = r
    return m


def integer_check(m, n):
    # Input: Two positive integers m and n
    # Output: Greatest common divisor of m and n
    if m < n:
        t = m
    else:
        t = n

    while t >= 0:
        if m % t == 0:
            if n % t == 0:
                return t
        t -= 1


def prime_factors(n):
    # Input: A positive integer
    # Output: All the prime factors of the input
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
    if n > 1:
        factors.append(n)
    return factors


def middle_school(m, n):
    # Input: Two positive integers m and n
    # Output: Greatest common divisor of m and n
    m_factors = prime_factors(m)
    n_factors = prime_factors(n)
    common_factors = []
    for x in m_factors:
        for y in n_factors:
            if x == y:
                n_factors.remove(y)
                common_factors.append(y)
                break
    out = 1
    for z in common_factors:
        out = out * z
    return out


def eff_gcd(s1, s2):
    t0 = time.perf_counter()
    gcd = euclid(s1, s2)
    t1 = time.perf_counter()
    elapsed = t1 - t0
    print("\nEuclid Algorithm:\nAnswer: " + str(gcd) + "\nTime elapsed: " + str(elapsed))

    t0 = time.perf_counter()
    gcd = integer_check(s1, s2)
    t1 = time.perf_counter()
    elapsed = t1 - t0
    print("\nConsecutive Integer Check Algorithm:\nAnswer: " + str(gcd) + "\nTime elapsed: " + str(elapsed))

    t0 = time.perf_counter()
    gcd = middle_school(s1, s2)
    t1 = time.perf_counter()
    elapsed = t1 - t0
    print("\nMiddle School Method:\nAnswer: " + str(gcd) + "\nTime elapsed: " + str(elapsed))


def main():
    error_count = 0
    while error_count < 3:
        i = input("Input a positive integer: ")
        j = input("Input a positive integer: ")
        try:
            s1 = int(i)
            s2 = int(j)
            if s1 <= 0 or s2 <= 0:
                raise ValueError
            eff_gcd(s1, s2)
            return 1

        except ValueError:
            print("Invalid input, try again!\n")
            error_count += 1

    print("Too many invalid inputs. Goodbye.")
    return 0


main()

'''
# Tests
print("Euclid algorithm: 60, 24: " + str(euclid(60, 24)))
print("Euclid algorithm: 20, 25: " + str(euclid(20, 25)))
print("Euclid algorithm: 120, 180: " + str(euclid(120, 180)))
print("Euclid algorithm: 49204, 329012: " + str(euclid(49204, 329012)))
print("Euclid algorithm: 49204, 329012: " + str(euclid(181427400, 25989600)))
print("Euclid algorithm: 129749, 429801: " + str(euclid(129749, 429801)) + "\n")

print("Consecutive Integer Check algorithm: 60, 24: " + str(integer_check(60, 24)))
print("Consecutive Integer Check algorithm: 20, 25: " + str(integer_check(20, 25)))
print("Consecutive Integer Check algorithm: 120, 180: " + str(integer_check(120, 180)))
print("Consecutive Integer Check algorithm: 49204, 329012: " + str(integer_check(49204, 329012)))
print("Consecutive Integer Check algorithm: 181427400, 25989600: " + str(integer_check(181427400, 25989600)))
print("Consecutive Integer Check algorithm: 129749, 429801: " + str(integer_check(129749, 429801)) + "\n")

print("Middle School algorithm: 60, 24: " + str(middle_school(60, 24)))
print("Middle School algorithm: 20, 25: " + str(middle_school(20, 25)))
print("Middle School algorithm: 120, 180: " + str(middle_school(120, 180)))
print("Middle School algorithm: 49204, 329012: " + str(middle_school(49204, 329012)))
print("Middle School algorithm: 181427400, 25989600: " + str(middle_school(181427400, 25989600)))
print("Middle School algorithm: 129749, 429801: " + str(middle_school(129749, 429801)) + "\n")
'''
