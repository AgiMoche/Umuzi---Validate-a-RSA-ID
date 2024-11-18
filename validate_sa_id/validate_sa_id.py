from datetime import datetime as dt


def check_if_id_number_is_string(id_number):
    return isinstance(id_number, str)


def check_if_id_number_has_13_characters(id_number):
    return len(id_number) == 13


def check_if_id_has_valid_citizenship_number(id_number):
    return id_number[-3] == "0" or id_number[-3] == "1"


def check_if_id_number_is_numeric(id_number):
    return id_number.isnumeric()


def check_birth_date(id_number):
    try:
        return bool(
            dt.strptime(
                "-".join([id_number[4:6], id_number[2:4], id_number[0:2]]), "%d-%m-%y"
            )
        )

    except:
        return False


def check_if_id_number_has_valid_checksum(id_number):
    luhns_output_list = []

    digits_input_list = []

    for number in id_number:
        digits_input_list.append(int(number))

    for index in range(len(id_number[0:-1])):
        if index % 2 == 0:
            luhns_output_list.append(digits_input_list[index])

        else:
            luhns_output_list.append(digits_input_list[index] * 2)

    luhns_sum = 0

    for number in luhns_output_list:
        if len(str(number)) != 1:
            for value in str(number):
                luhns_sum += int(value)

        else:
            luhns_sum += number

    luhns_outcome_check = 10 - (luhns_sum % 10)

    return id_number[-1] == str(luhns_outcome_check)


def is_id_number_valid(id_number):
    return (
        check_if_id_number_is_string(id_number)
        and check_if_id_number_is_numeric(id_number)
        and check_if_id_number_has_13_characters(id_number)
        and check_birth_date(id_number)
        and check_if_id_has_valid_citizenship_number(id_number)
        and check_if_id_number_has_valid_checksum(id_number)
    )
