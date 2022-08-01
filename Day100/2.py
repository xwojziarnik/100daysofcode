"""
Task2:
Create a function which gets length of base and a height of a triangle and prints field of that triangle.
"""


def get_triangle_field(base: int, height: int) -> float:
    print(0.5 * base * height)


def test_get_triangle_field(capsys):
    # given:
    base = 10
    height = 8

    # when:
    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    # then:
    assert out == '40.0\n'  # print is adding '\n' at the end of the line!
