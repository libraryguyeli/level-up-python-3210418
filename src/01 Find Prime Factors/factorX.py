def get_prime_factors(num: int):
  factors = []
  factor = 2
  while (num >= 2):
    if num % factor == 0:
      factors.append(factor)
      num = num / factor
    else:
      factor += 1
  return factors

print(get_prime_factors(13)) # [13]
print(get_prime_factors(60)) # [2, 2, 3, 5]
print(get_prime_factors(630)) # [2, 3, 3, 5, 7]
print(get_prime_factors(0)) # []