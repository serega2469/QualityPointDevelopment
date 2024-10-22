"""
Консольное приложение.
Вводить ЦЕЛЫЕ числа, пока не будет введен ноль. Вывести число с максимальной суммой цифр в нем.
"""


def get_sum_digits(number: int) -> int:
    if number < 0:
        return 0

    total: int = 0
    while number > 0:
        total += number % 10
        number //= 10

    return total


def main() -> None:
    num_with_max_sum_digits = max_num = 0
    while True:
        num: int = int(input())

        if num == 0:
            break

        temp: int = get_sum_digits(num)

        if temp > num_with_max_sum_digits:
            num_with_max_sum_digits = temp
            max_num = num

    print(max_num)


if __name__ == "__main__":
    main()

