import pytest

from validate_sa_id.validate_sa_id import is_id_number_valid


@pytest.mark.parametrize(
    "input_for_validation_function, output_for_validation_function",
    [(2909035800085, False), ("2909035800085", True)],
)
def test_check_if_id_number_is_string(
    input_for_validation_function, output_for_validation_function
):
    assert (
        is_id_number_valid(input_for_validation_function)
        == output_for_validation_function
    )


@pytest.mark.parametrize(
    "input_for_validation_function, output_for_validation_function",
    [("980203", False), ("2909035800085", True)],
)
def test_check_if_id_number_has_13_characters(
    input_for_validation_function, output_for_validation_function
):
    assert (
        is_id_number_valid(input_for_validation_function)
        == output_for_validation_function
    )


@pytest.mark.parametrize(
    "input_for_validation_function, output_for_validation_function",
    [("29B9035800085", False), ("2909035800085", True)],
)
def test_check_birth_date_input(
    input_for_validation_function, output_for_validation_function
):
    assert (
        is_id_number_valid(input_for_validation_function)
        == output_for_validation_function
    )


@pytest.mark.parametrize(
    "input_for_validation_function, output_for_validation_function",
    [
        ("29B9035800085", False),
        (2909035800085, False),
        ("2909035800085", True),
    ],
)
def test_check_if_id_number_is_numeric(
    input_for_validation_function, output_for_validation_function
):
    assert (
        is_id_number_valid(input_for_validation_function)
        == output_for_validation_function
    )


@pytest.mark.parametrize(
    "input_for_validation_function, output_for_validation_function",
    [("2909035800385", False), ("2909035800085", True)],
)
def test_check_if_id_has_valid_citizenship_number(
    input_for_validation_function, output_for_validation_function
):
    assert (
        is_id_number_valid(input_for_validation_function)
        == output_for_validation_function
    )


@pytest.mark.parametrize(
    "input_for_validation_function, output_for_validation_function",
    [("2909035800089", False), ("2909035800085", True)],
)
def check_if_id_number_has_valid_checksum(
    input_for_validation_function, output_for_validation_function
):
    assert (
        is_id_number_valid(input_for_validation_function)
        == output_for_validation_function
    )
