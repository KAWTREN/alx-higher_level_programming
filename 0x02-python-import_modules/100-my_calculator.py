#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from  calculator_1 import  add, sub, mul, div

    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    op = sys.argv[2]
    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
        exit(0)
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
        exit(0)
    elif op == "*":
        print("{} * {} = {}".format(a, mul(a, b)))
        exit(0)
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
