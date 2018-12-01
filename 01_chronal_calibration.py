import fileinput


def cal_repeating_freq(input_file):
    result = 0
    seen = {}

    while True:
        for line in fileinput.input(input_file):
            result += int(line)

            if str(result) in seen:
                return result

            seen[str(result)] = 1


print(cal_repeating_freq('input/01'))
