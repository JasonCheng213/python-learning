'''
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
import random


def create_cde():
    code = ""
    for index in range(0, 16):
        code += str(random.randint(0, 9))
    return code


for i in range(0, 200):
    print("%s -- %s" % (i, create_cde()))
