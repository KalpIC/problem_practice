def mul():
    var_1 = int(input("var 1"))
    var_2 = int(input("var 2"))
    return var_1 * var_2


if __name__ == "__main__":
    mul_1 = mul()
    if mul_1 == 0:
        print("It's Zero")
    else:
        print("Not Zero")

