from argparse import ArgumentParser
from typing import Union

parser = ArgumentParser(description="")
parser.add_argument(
    "Expression",
    type=str,
    help="Input string to calculator. Either to be evaluated by the "
    "calculator (default) or to be requested to WolframAlpha.",
)
parser.add_argument(
    "-w",
    type=bool,
    default=False,
    help="Send input to WolframAlpha or not. Default is false",
)
args = parser.parse_args()


def calculate(expression: str) -> Union[int, float]:
    return eval(expression)


if __name__ == "__main__":
    ans = calculate(args.Expression)
    print(ans)
