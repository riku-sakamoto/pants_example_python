import pytest

from fizzbuzz import FizzBuzzRunner


@pytest.mark.parametrize(
    "div1, div2, number, expected",
    [(3, 5, 11, "11"), (3, 5, 6, "Fizz"), (3, 5, 10, "Buzz"), (3, 5, 15, "FizzBuzz")],
)
def test__runner_run(div1, div2, number, expected):
    runner = FizzBuzzRunner(div1, div2)

    actual = runner.run(number)
    assert actual == expected


@pytest.mark.parametrize("div1, div2", [(3, 6), (12, 16)])
def test__cannot_initialized(div1, div2):
    with pytest.raises(ValueError):
        _ = FizzBuzzRunner(div1, div2)
