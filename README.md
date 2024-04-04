# Boolean Options to Int

Have you ever dreamt of storing up to 62 boolean options with just two numbers? Dream no more!

This project is an experimentation of bitwise operations.

## Files

### `boolean_options_converter.py`

Provides `get_calculated_code_from_boolean_options` and `get_calculated_options_from_code` functions.

Example:

```python
options = [True, False, True, False, True, True]

# BooleanOptionsCode(number=53, length=6)
calculated_code = get_calculated_code_from_boolean_options(options)
```

```python
code = BooleanOptionsCode(number=3, length=2)

# [True, True]
calculated_options = get_calculated_options_from_code(code)
```

### `test_boolean_options_converter.py`

Provides testing. Run with `python3 test_boolean_options_converter.py`

### `demonstration.py`

Provides a demonstration of the benefits

Current output:

```
**** Demonstration ****
1. Conversion
    - Here's one big list of options                       -> [True, False, True, False, True, True, True, True, True, True, False, False, False, False, True, True, False, True, True, False, True, True, False, True, True, False]
    - Here's the calculated code                           -> BooleanOptionsCode(number=28754933, length=26)
    - Wait? Do we get the same options back using the code -> True

2. Size improvement
    - Here is the size of the options list (in RAM)                     -> 264
    - Here is the size of the options list string in UTF-8 (in storage) -> 52
    - Here is the size of the code object  (in RAM)                     -> 56
    - Here is the size of the code object string in UTF-8 (in storage)  -> 11
```
