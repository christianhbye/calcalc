import requests
from typing import Union
import urllib.parse


def _calculate(expression: str) -> Union[int, float]:
    """
    Evaluate a mathematical expression in Python with the built-in eval()

    Params:
    expression: str, the mathematical expression to evaluate

    Returns:
    A number (float or int), the output of the calculation
    """
    return eval(expression)

def _ask_wolfram(expression: str) -> Union[int, float]:
    """
    Use Wolfram Alpha to answer the question of the string
    """
    APP_ID='GETY26-72YYRUHXPV'
    url_exp=urllib.parse.quote_plus(expression)  # convert to url format
    url=f'http://api.wolframalpha.com/v2/query?input={url_exp}&appid={APP_ID}'\
            f'&format=plaintext&output=json'
    r = requests.get(url).json()
    d = r['queryresult']['pods'][0]['subpods'][0]
    return d['plaintext']  # need to add some code here

def calculate(expression: str, wolfram: bool = False) -> Union[int, float]:
    """
    Evaluate a mathematical expresison or answer a question to wolfram
    
    Params:
    expression: str, the mathematical expression to evaluate OR a question
    to be answered by Wolfram Alpha
    wolfram: bool, whether to ask wolfram alpha the question. Default is False.
    
    Returns:
    int or float, the output of the calculation
    """
    if not wolfram:  # use Python
        return _calculate(expression)
    else:  # use Wolfram
        return _ask_wolfram(expression)


if __name__ == "__main__":
    from argparse import ArgumentParser
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
    ans = calculate(args.Expression, args.w)
    print(ans)
