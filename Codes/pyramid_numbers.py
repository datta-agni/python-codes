# Pyramid of Natural Numbers Less Than 10
# Pattern:
# 1
# 2 3 4
# 5 6 7 8 9

currentNumber = 1
stop = 2
rows = int(input("ENTER THE NUMBER OF ROWS:"))
# Rows you want in your pattern

for i in range(rows):

    for column in range(1, stop):
        print(currentNumber, end='')

        currentNumber += 1

    print('')

    stop += 2
