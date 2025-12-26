def expand_pid_range(pid_range):
    """
    Returns a list of integers based from the product ID range given.

    :param pid_range: Range of product IDs
    :type pid_range: str, required

    :returns: A list of product IDs
    :rtype: [int]
    """
    pid_range = pid_range.split('-')
    product_ids = range(int(pid_range[0]), int(pid_range[1])+1)

    return product_ids

def is_pid_invalid(pid):
    """
    A product ID is invalid if it is made only of some sequence of digits repeated twice. 
    55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
    101 is a valid ID.

    :param pid:
    :type pid: int

    :returns: True if product ID is invalid, otherwise False
    :rtype: bool
    """
    pid = str(pid)

    if len(pid)%2 != 0:
        return False

    midpoint = int(len(pid)/2)
    if pid[0:midpoint] == pid[midpoint:]:
        return True
    else:
        return False

def is_pid_invalid_v2(pid):
    """
    A product ID is invalid if it is made only of some sequence of digits repeated at least twice.
    12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

    :param pid:
    :type pid: int

    :returns: True if product ID is invalid, otherwise False
    :rtype: bool
    """
    pid = str(pid)

    # Hardcoded rule, these product ids are not invalid
    if int(pid) <= 10:
        return False

    # If the number of digits are odd, then it will only be invalid if all digits are the same
    if len(pid)%2 != 0:
        if len(set(pid)) == 1:
            return True

    # Split the product id into two, if both halves are equal, then they are invalid
    midpoint = int(len(pid)/2)
    if pid[0:midpoint] == pid[midpoint:]:
        return True
    
    # Given a product id 123412341234:
    #   split(12) -> ['', '34', '34', '34']
    #       unique_elemtents = 2, continue and increment split value
    #   split(123) -> ['', '4', '4', '4']
    #       unique_elemtents = 2, continue and increment split value
    #   split(1234) -> ['', '', '', '']
    #       unique_elemtents = 1, stop, product id is invalid
    for i in range(0, midpoint):
        possible_patterns = set(pid.split(pid[0:i+1]))
        if len(possible_patterns) == 1:
            return True

    return False

        
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for line in f:
            pid_ranges = line.strip('\n')

    pid_sum = 0

    for pid_range in pid_ranges.split(','):
        for pid in expand_pid_range(pid_range):
            # if is_pid_invalid(pid):
            if is_pid_invalid_v2(pid):
                pid_sum += pid

    print(pid_sum)