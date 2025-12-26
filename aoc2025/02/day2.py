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
    

    return True


if __name__ == '__main__':

    with open('test2.txt', 'r') as f:
        for line in f:
            pid_ranges = line.strip('\n')

    for pid_range in pid_ranges.split(','):
        for product_id in expand_pid_range(pid_range):
            print(product_id, (is_pid_invalid(product_id)))


        print('----')