from argparse import ArgumentParser

parser=ArgumentParser(description='')
parser.add_argument('Expression', metavar='E', type=str)
args=parser.parse_args()

def calculate(expression):
    return eval(expression)

if __name__=='__main__':
    ans=calculate(args.Expression)
    print(ans)

