from collections import namedtuple
import enum

Rotation = namedtuple('Rotation', ['direction', 'distance'])


def parse_rotation(rotation_string):
    """
    Parse the distance and direction of rotation from the given string.

    :param rotation_string: Rotation instruction in the format of "R10" or "L25"
    :type rotation_string: str, required

    :returns: Rotation namedtuple with the direction and distance
    :rtype: Rotation

    :raises ValueError: If rotation_string is empty, or has an invalid format
    """
    rotation_string = rotation_string.strip()

    if not rotation_string:
        raise ValueError("Rotation string cannot be an empty.")

    if len(rotation_string) < 2:
        raise ValueError("Rotation string length is incorrect; format must be: R25 or L10")

    direction = rotation_string[0].upper()
    if direction not in ['L', 'R']:
        raise ValueError("Rotation string direction should either be L or R.")

    try:
        distance = int(rotation_string[1:])
    except ValueError as e:
        raise ValueError(f"Cannot parse {rotation_string[1:]} to integer.")

    if distance < 0:
        raise ValueError("Rotation string distance must be non-negative.")

    return Rotation(direction, distance)


def rotate(direction, distance, pointer_values, pointer_curr_value):
    """
    Rotates the pointer based from the direction and distance given.

    :param direction: L for left (decrease) or R for right (increase)
    :type direction: str, required
    :param distance: The number of times the pointer will have to move
    :type distance: int, required
    :param pointer_values: The list of values that the pointer will rotate to
    :type pointer_values: list, required
    :param pointer_curr_value: Current value selected by the pointer
    :type pointer_curr_value: int, required

    :returns: A tuple of the current value of the pointer and how many times it pointed to zero
    :rtype: tuple
    """

    curr_idx = pointer_values.index(pointer_curr_value)
    number_cnt = 0

    for i in range(0, distance):
        if direction == 'R':
            curr_idx += 1
            if curr_idx == len(pointer_values):
                curr_idx = 0
        else:
            curr_idx -= 1
            if curr_idx < 0:
                curr_idx = len(pointer_values)-1
        
        if pointer_values[curr_idx] == 0:
            number_cnt +=1

    return pointer_values[curr_idx], number_cnt


with open('input.txt', 'r') as file:
    zero_count = 0
    pointer_values = range(0, 100)
    pointer_start = 50
    for line in file:
        movement = parse_rotation(line.strip('\n'))
        ptr = rotate(movement.direction, movement.distance, pointer_values, pointer_start)
        pointer_start = ptr[0]
        zero_count += ptr[1]
        
    print(zero_count)





