import numpy as np


class FizzBuzzRunner:
    def __init__(self, div1: int, div2: int) -> None:
        self._div1 = div1
        self._div2 = div2

    def __post_init__(self):
        gcd_val = np.gcd.reduce([self._div1, self._div2])
        if np.testing.assert_almost_equal(gcd_val, 1.0):
            return

        raise ValueError(
            f"gcd for {self._div1} and {self._div2} is not equal to 1 ."
        )

    def run(self, number: int) -> str:
        if number % self._div1 == 0:
            return "Fizz"

        if number % self._div2 == 0:
            return "Buzz"
        
        if number % (self._div1 * self._div2) == 0:
            return "FizzBuzz"
        
        return f"{number}"


if __name__ == "__main__":
    runner = FizzBuzzRunner(3, 5)
    for i in range(1, 101):
        s = runner.run(i)
        print(s)
