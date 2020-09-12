# PF-Assgn-38

def check_double(number):
    return True if ("".join(sorted(str(number))) == "".join(sorted(str(number*2)))) else False


print(check_double(125874))
