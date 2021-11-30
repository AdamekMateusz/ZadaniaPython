import math

class Style:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_factors():
    factor = []
    for i in range(3):
        number = input(f'Get factor {chr(97+i)}: ')
        try:
            number = int(number)
        except ValueError:
            print(Style.FAIL, "Cannot convert input value to integer, script cannot continue", Style.RESET)
            exit(0)
        else:
            factor.append(number)
    return factor

def calculate_delta(factors):
    a = factors[0]
    b = factors[1]
    c = factors[2]

    return b**2 - 4*a*c

def get_root(delta, factors):
    a = factors[0]
    b = factors[1]
    c = factors[2]
    if delta < 0:
        print(Style.WARNING, "Cannot calcualte root of equation,\n delta is less than zero ", Style.RESET)
        return None
    elif delta == 0:
        return -a/(2*b)

    else:
        root_1 = (-b - math.sqrt(delta))/(2*a)
        root_2 = (-b + math.sqrt(delta))/(2*a)
        return root_1, root_2

if __name__ == '__main__':
    factor = get_factors()
    delta = calculate_delta(factor)
    roots = get_root(delta, factor)

    if roots is not None:  print(Style.GREEN,roots,Style.RESET) 

