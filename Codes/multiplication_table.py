# Multiplication table (from 1 to 100)

num = float(input("DISPLAY MULTIPLICATION TABLE OF? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 101):
    print(num, 'x', i, '=', num * i)
