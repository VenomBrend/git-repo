print("type integers, each followed by enter; or just enter to finish")

count = 0
sum = 0
min = max = 0

while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        sum += number
        count += 1
    else:
        break

if count:
    print("count: ", count, " sum: ", sum)

input()
