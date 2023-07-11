def solution(people, limit):

    my_list = people
    kg = limit
    count = 0

    while True:
        if len(my_list) == 0:
            return count
        x = my_list[0]
        kg -= x
        my_list.remove(x)
        for i in my_list:
            if i <= kg:
                my_list.remove(i)
                break

        count += 1
        kg = limit

    return count