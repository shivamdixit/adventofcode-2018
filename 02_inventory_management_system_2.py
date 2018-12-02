import fileinput

# cache the list of IDs from file to avoid multiple File I/O
id_list = []
for line in fileinput.input():
    id_list.append(line.rstrip())

# compare every string with every other: O(n^2)
for i, string_1 in enumerate(id_list):
    for j, string_2 in enumerate(id_list[i + 1:]):
        difference = 0
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                difference += 1

            # only difference of 1 is allowed
            if difference > 1:
                break

        if difference == 1:
            # assuming there will only be one such case
            print('First string:{}, second string: {}'.format(string_1, string_2))
            break
