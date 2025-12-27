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
                return LargestDigit(idx, num[idx])


if __name__ == '__main__':
    total_joltage = 0
    with open('input.txt', 'r') as f:
        for line in f:
            banks = line.strip('\n')

            first_battery_search = banks[0:len(banks)-1]  # get all batteries except the last one
            battery_1 = find_largest_digit_pos(first_battery_search)

            second_battery_search = banks[battery_1.position+1:] # get batteries to the right of battery_1
            battery_2 = find_largest_digit_pos(second_battery_search)

            combined_batt = battery_1.value + battery_2.value
            total_joltage += int(combined_batt)

        print(total_joltage)