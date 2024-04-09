import re
from typing import List, Union


def check_float(string):
    pattern = r"^[0-9]*\.?[0-9]+$"
    match = re.match(pattern, string)

    return bool(match)


def check_int(string):
    return string.isdigit()


def validate_numbers(user_numbers: List[str]):
    for user_number in user_numbers:
        if not check_int(user_number):
            raise ValueError('Число должно быть целое')


def validate(distance: str):
    is_int = check_int(distance)
    is_float = check_float(distance)

    if not is_float and not is_int:
        raise ValueError('Необходимо передать только положительное число')

    return is_int, is_float


def prepare_number(distance: str):
    is_int, _ = validate(distance)

    return int(distance) if is_int else float(distance)


def get_distances_with_new_cash_machine(
        l_distances: List[Union[int, float]],
        count_new_cash_machine: int
):
    for _ in range(count_new_cash_machine):

        max_distance: Union[int, float] = max(l_distances)
        index_max_distance: int = l_distances.index(max_distance)
        new_distance: float = max_distance / 2

        if new_distance.is_integer():
            new_distance = int(new_distance)

        l_distances.remove(max_distance)
        l_distances.insert(index_max_distance, new_distance)
        l_distances.insert(index_max_distance + 1, new_distance)

    return l_distances


if __name__ == '__main__':
    user_numbers = input('Введите два числа через пробел: ').split()

    validate_numbers(user_numbers)

    n_count_cash_machines, k_new_cash_machines = tuple(map(int, user_numbers))

    l_distances = []

    for _ in range(n_count_cash_machines):
        distance = input('Введите расстояние: ')

        number: Union[int, float] = prepare_number(distance)

        l_distances.append(number)

    new_distances: List[int, float] = get_distances_with_new_cash_machine(l_distances, k_new_cash_machines)

    for distance in new_distances:
        print(distance, end='\n')