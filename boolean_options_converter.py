from dataclasses import dataclass, field
from typing import Union
from copy import copy


# We need to specify the length to fill in final False options
@dataclass
class BooleanOptionsCode:
    number: int = field(kw_only=True)
    length: int = field(kw_only=True)

    def __post_init__(self) -> None:
        if self.number < 0 or self.length < 0:
            raise ValueError("The number and the length must be positive (>=0)")


def get_corrected_options_with_remaining_falses(options: list[bool], remaining_falses: int) -> list[bool]:
    options = copy(options)

    options.extend([False for _ in range(remaining_falses)])

    return options


def get_calculated_code_from_boolean_options(options: list[bool]) -> BooleanOptionsCode:
    option_numbers_with_applied_coefficients = (
        int(option) * (2**index)
        for index, option in enumerate(options)
    )

    code = BooleanOptionsCode(
            number=sum(option_numbers_with_applied_coefficients),
            length=len(options)
    )

    return code



def get_calculated_options_from_code(code: BooleanOptionsCode) -> list[bool]:
    current_code = copy(code)
    options = []

    while True:
        # Check if last bit is 1 -> True option
        current_option = current_code.number & 1
        options.append(bool(current_option))

        # Shift right one bit
        current_code.number >>= 1
        current_code.length -= 1

        if not current_code.number:
            # The code can have a length > 0 because of remaining False options
            options = get_corrected_options_with_remaining_falses(
                    options,
                    current_code.length
            )

            return options
