import fileinput

two_counts = 0
three_counts = 0
for line in fileinput.input():
    counter = {}

    for char in line.rstrip():
        if char in counter:
            counter[char] += 1

        else:
            counter[char] = 1

    counted_for_two = 0
    counted_for_three = 0
    for char, count in counter.items():
        if count == 2 and not counted_for_two:
            two_counts += 1
            counted_for_two = 1

        if count == 3 and not counted_for_three:
            three_counts += 1
            counted_for_three = 1

        if counted_for_two and counted_for_three:
            break


print(two_counts * three_counts)
