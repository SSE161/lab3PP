import re

regex = "([0-9]{1,3}[\.]){3}[0-9]{1,3}"


def ip_checker(string):
    o = re.match(regex, string)
    if o is None:
        return False
    else:
        return True


def ip_finder(string):
    o = re.search(regex, string)
    if o is None:
        return None
    else:
        return o


print(ip_checker("192.168.0.1"))
print(ip_finder("jcnncjdnceencneuneu192.168.0.1uduu3h3fhh38h8f")[0])
