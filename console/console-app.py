# -*- coding:utf-8 -*-
"""计算器使用帮助.

命令格式 [-n number | -o operation].

-n    : 待计算数
-o    : 操作符

例子： -n 1 -n 2 -o +
"""
import getopt
import sys


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def calculator(num1, num2, operation):
    if num1 is not None and num2 is not None and operation is not None:
        num1 = int(num1)
        num2 = int(num2)
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
    return result


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hn:o:", ["help", "number", "operation"])
        except getopt.error as ex:
            raise Usage(ex)
        operation = None
        num1 = None
        num2 = None
        for opt, arg in opts:
            if opt == "-h" or opt == "--help":
                usage()
                return 0
            elif opt == "-n" or opt == "--number":
                if num1 is None:
                    num1 = arg
                elif num2 is None:
                    num2 = arg
                else:
                    raise Usage("最多支持两个数字的计算")
            elif opt == "-o" or opt == "--operation":
                operation = arg
                if operation not in ["+", "-", "*", "/"]:
                    raise Usage("不支持操作符: %s" % operation)
            print("结果：%s %s %s = %s" % (num1, operation, num2, calculator(num1, num2, operation)))
    except Usage as ex:
        print(ex)
        print("for help use --help")
        return 2


def usage():
    print(__doc__)


if "__main__" == __name__:
    sys.exit(main())
