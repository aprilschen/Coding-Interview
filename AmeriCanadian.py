def driver():
    str = input()
    while str != "quit!":
        output = AmeriCanadian(str)
        print(output)
        str = input()

def AmeriCanadian(str):
    if len(str) > 4 and str[-3] not in "aeiouy" and str[-2:] == "or":
        return str[0:-2] + "our"
    return str

driver()


