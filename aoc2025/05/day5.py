import sqlite3
from collections import namedtuple
Rng = namedtuple('Rng', ['lower', 'upper'])


if __name__ == '__main__':
    is_ingredient_id = False
    fresh_ing_list = []
    available_fresh_cnt = 0

    with open('input2.txt', 'r') as file:
        for f in file:
            line = f.strip('\n')
            rng = line.split('-')

            fresh_ing_list.append(rng)

    # print(fresh_ing_list)

    for idx, i in enumerate(fresh_ing_list):
        if i[0] == 'x' and i[1] == 'x':
            continue
        for jdx, j in enumerate(fresh_ing_list):
            if jdx == idx:
                continue

            control_lower = i[0]
            control_upper = i[1]
            exp_lower = j[0]
            exp_upper = j[1]

            if exp_lower == 'x' and exp_upper == 'x':
                continue

            # print(f"{i} vs {j}")

            if exp_lower >= control_lower and exp_upper <= control_upper:
                fresh_ing_list[jdx][0] = 'x'
                fresh_ing_list[jdx][1] = 'x'

            if exp_lower >= control_lower and exp_lower <= control_upper and exp_upper > control_upper:
                fresh_ing_list[jdx][0] = str(int(control_upper)+1)
                fresh_ing_list[jdx][1] = str(int(control_upper) + (int(exp_upper)-int(control_upper)))

            if exp_upper >= control_lower and exp_upper <= control_upper and exp_lower < control_lower:
                fresh_ing_list[jdx][1] = exp_lower
                fresh_ing_list[jdx][1] = str(int(control_lower)-1)


            # print(fresh_ing_list)

    for i in fresh_ing_list:
        if i[0] == 'x':
            continue

        available_fresh_cnt += len(range(int(i[0]), int(i[1])+1))

    print(available_fresh_cnt)

    # for idx, i in enumerate(fresh_ing_list):
    #     if i[0] == 'x' and i[1] == 'x':
    #         continue
    #     j = idx+1
    #     while j < len(fresh_ing_list):
    #         control_lower = i[0]
    #         control_upper = i[1]
    #         exp_lower = fresh_ing_list[j][0]
    #         exp_upper = fresh_ing_list[j][1]

    #         if exp_lower == 'x' and exp_upper == 'x':
    #             j +=1
    #             continue

    #         print(f"{i} vs {fresh_ing_list[j]}")

    #         if exp_lower >= control_lower and exp_upper < control_upper:
    #             fresh_ing_list[j][0] = 'x'
    #             fresh_ing_list[j][1] = 'x'

    #         print(fresh_ing_list)
    #         j +=1


    #         # # Part 1
    #         # if line == '':
    #         #     is_ingredient_id = True
    #         #     continue

    #         # if is_ingredient_id:
    #         #     for i in fresh_ing_list:
    #         #         if int(line) in range(i.lower, i.upper+1):
    #         #             available_fresh_cnt += 1
    #         #             break
    #         # else:
    #         #     rng = line.split('-')
    #         #     fresh_ing_list.append(Rng(lower=int(rng[0]), upper=int(rng[1])))

    # # print(len(set(fresh_ing_list)))