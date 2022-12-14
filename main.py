import re

regex = "([0-9]{1,3}[\.]){3}[0-9]{1,3}"


def ip_checker(string):
    o = re.match(regex, string)
    if o is None:
        return False
    else:
        return True


print(ip_checker("192.168.0.1"))
