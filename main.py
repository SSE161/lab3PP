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

k="word: hello"
l="192.168.0.1"
print(k + " is a valid IP address: " + str(ip_checker(k)))
print(l + " is a valid IP address: " + str(ip_checker(l)))
j="jcnncjdnceencneuneu192.168.0.1uduu3h3fhh38h8f"
print("in " + j+ " found " + ip_finder(j)[0])

