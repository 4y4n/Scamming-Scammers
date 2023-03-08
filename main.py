import requests
import time
import random


def generateUser():
    email = []
    options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', '-', '-', '-', '-', '_', '_', '_', '_', 'b', 'c',
               'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']
    for i in range(10):
        char = options[random.randint(0, len(options)-1)]
        upper = bool(random.getrandbits(1))
        if not char.isdigit() and upper:
            char = char.upper()
        email.append(char)
    return "".join(email)


def generatePass():
    password = []
    options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    for i in range(20):
        char = options[random.randint(0, len(options) - 1)]
        upper = bool(random.getrandbits(1))
        if upper:
            char = char.upper()
        password.append(char)
    return "".join(password)


url = "https://shraidar.org/new_login.php"  # action url in html form tag that input is posted to
inUser = 'email'  # name associated with username input tag
inPass = 'pass'  # name associated with password input tag

while True:

    username = generateUser()
    password = generatePass()
    print("Sending: \t" + username + "\t\t" + password)

    payload = {
        inUser: username,
        inPass: password
    }

    with requests.Session() as s:
        p = s.post(url, data=payload)
    time.sleep(0.5)
