import argparse

from utils import show_format_str

from fizzbuzz import FizzBuzzRunner


def _init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int, default=20)
    parser.add_argument(
        "--show-fizzbuzz", action="store_true", help="If True, show fizzbuzz"
    )
    return parser


def main():
    parser = _init_argparse()
    args = parser.parse_args()

    if args.show_fizzbuzz:
        runner = FizzBuzzRunner(3, 5)

        for i in range(args.start, args.stop):
            val = runner.run(i)
            show_format_str(val)


if __name__ == "__main__":
    main()
