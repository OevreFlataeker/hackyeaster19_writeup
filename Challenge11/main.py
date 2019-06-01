import requests

# Use burp
# Use "proxies = {}" when you don't want to use burp

proxies = {
  'http': 'http://127.0.0.1:8080',
  'https': 'http://127.0.0.1:8080',
}
mainpage_req = requests.get('http://whale.hacking-lab.com:1111/',proxies=proxies)

for rnd in range(1,11):
    print("Round: ", rnd)
    pairs={}
    for i in range(1,99):
        p_res = requests.get('http://whale.hacking-lab.com:1111/pic/'+str(i),cookies=mainpage_req.cookies,proxies=proxies, stream=True)
        s = len(p_res.content)
        if not s in pairs.keys():
            pairs[s]=[i]
        else:
            pairs[s].append(i)
        del p_res
    print("Done!")

    for k in pairs.keys():
        payload = {'first': pairs[k][0], 'second': pairs[k][1]}
        r = requests.post('http://whale.hacking-lab.com:1111/solve', data=payload, proxies=proxies, cookies=mainpage_req.cookies)
        print(r.text)