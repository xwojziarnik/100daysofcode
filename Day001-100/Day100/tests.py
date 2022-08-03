"""This is the last day of #100daysofcode challenge. Today I'm going to repeat material about testing in Python."""

"""
Useful commands:
pip3 install pytest         -> install pytest module (if you use Windows OS type pip install pytest)
pytest <file_name>.py       -> run tests for specific file,
pytest -k 'special_run'     -> run every test that has 'special run' in its name,
pytest -m 'marker_name'     -> run tests that are decorated by 'marker_name' decorator
"""

# Assert:
"""
If result of assert statement is true - user won't see any error, 
but if result is false, user will see an AssertionError.
"""

result = 5

assert result < 5
assert 5 == result
assert result is True
assert result is False or result == 34
