
def domath(func,z):
    y=func(z)
    return y


def mathfunc1(x):
    return b * (x ** 2)


def main():

    def mathfunc2(z):
        return b * (z ** 3)

    a=5
    b=3
    answer=domath(mathfunc1,3.1)
    print(answer)
    answer2=domath(mathfunc2,4.8)

    print(answer2)
    answer3=domath(lambda x: a* x**3,4.8)
    print(answer3)

main()
