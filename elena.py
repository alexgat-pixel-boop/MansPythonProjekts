name = input("Ievadiet savu vārdu: ")
print(f"Sveiks, {name}!")

print("Ievadiet piecus skaitļus pa vienam:")
numbers = []
for i in range(5):
    number = float(input(f"Ievadiet {i + 1}. skaitli: "))
    numbers.append(number)

print(f"Jūsu sākotnējais saraksts: {numbers}")
sorted_numbers = sorted(numbers)
print(f"Sakārtots saraksts: {sorted_numbers}")
average = sum(numbers) / len(numbers)
print(f"Vidējā vērtība: {average}")
