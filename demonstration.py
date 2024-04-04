from boolean_options_converter import get_calculated_options_from_code, get_calculated_code_from_boolean_options
import sys

def run_demonstration():
    options = [True, False, True, False, True, True, True, True, True, True, False, False, False, False, True, True, False, True, True, False, True, True, False, True, True, False]

    calculated_code = get_calculated_code_from_boolean_options(options)

    calculated_options = get_calculated_options_from_code(calculated_code)


    print(f"""
**** Demonstration ****
1. Conversion
    - Here's one big list of options                       -> {options}
    - Here's the calculated code                           -> {calculated_code}
    - Wait? Do we get the same options back using the code -> {options == calculated_options}

2. Size improvement
    - Here is the size of the options list (in RAM)                     -> {sys.getsizeof(options)}
    - Here is the size of the options list string in UTF-8 (in storage) -> {2*len(options)}
    - Here is the size of the code object  (in RAM)                     -> {sys.getsizeof(calculated_code)}
    - Here is the size of the code object string in UTF-8 (in storage)  -> {len(str(calculated_code.length)) + len(str(calculated_code.number)) + 1}
      """)

if __name__ == "__main__":
    run_demonstration()
