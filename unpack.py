# def total(galleons, sickles, knuts=9):
#     return (galleons * 17 + sickles) * 29 + knuts


# # coins = (100, 20, 50)
# # print(total(*coins), "Knuts")
# coins = {"galleons": 100, "knuts": 20, "sickles": 50}
# print(total(**coins), "Knuts")


def f(*args, **kwargs):
    print("Positional ", args)
    print("Named: ", kwargs)


f(1, True, "Hello", 23.4578 + 234j, galleons=50)
