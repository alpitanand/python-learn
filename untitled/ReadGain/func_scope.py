def spam1():

    def spam2():

        def spam3():
            z = 'Even more spam'
            z += y
            return z
        y = 'More spam'+x
        y += spam3()
        return y
    x = 'spam'
    x += spam2()
    print("Locals {}".format(locals()))
    return x
print(spam1())
