def number_printer(max_number=100):
    two_multiple_msg = "buzz"
    five_multiple_msg = "bazz"
    for number in range(1, max_number + 1):
        message = str(number)
        if number % 2 == 0:
            message += two_multiple_msg
        if number % 5 == 0:
            message += five_multiple_msg
        print(message)  # noqa: WPS421


if __name__ == "__main__":
    number_printer()
