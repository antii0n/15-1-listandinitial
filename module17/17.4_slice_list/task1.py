import random

original_prices = [random.randint(-20, 20) for _ in range(10)]
new_prices = [i if i > 0 else 0 for i in original_prices]
print(original_prices)
print(new_prices)
print("Мы потеряли: ", abs(sum(original_prices) - sum(new_prices)))
