from collections import namedtuple

LargestDigit = namedtuple('LargestDigit', ['position', 'value'])

def find_largest_digit_pos(num):
    """
    Finds the first instance of the largest digit from the given number and 
    returns its index (position)

    :param num: Number to be searched
    :type num: int, required

    :returns: Index of the largest digit
    :rtype: int
    """
    

    num = str(num)

    for i in range(9, 0, -1):
        for idx, digit in enumerate(num):
            if int(digit) == i:
                return LargestDigit(int(idx), int(num[idx]))


if __name__ == '__main__':
    batteries_required = 12
    joltages = []
    

    with open('input.txt', 'r') as f:
        for line in f:
            banks = line.strip('\n')
            search_idx_start = 0
            search_idx_end = len(banks)-(batteries_required-1)
            battery_jolt = ""
            
            for i in range(0, batteries_required):
                search_radius = banks[search_idx_start:search_idx_end]
                battery = find_largest_digit_pos(search_radius)
                search_idx_start = search_idx_start + battery.position + 1
                search_idx_end += 1
                battery_jolt += str(battery.value)

            joltages.append(int(battery_jolt))

        print(sum(joltages))