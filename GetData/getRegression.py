import requests
import json

url = "https://pv.github.io/numpy-bench/regressions.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
}

proxies={
'http': None,
'https': '127.0.0.1:10809'  # https -> http
}

r = requests.get(url=url, headers=headers, proxies=proxies)
results = r.json()['regressions']

dict = {}
trans = {
    "0.29.21": "Param0",
    "0.29.27": "Param1",
    "0.29.14": "Param2"
}
with open("./temp.json") as fp:
    temp = json.load(fp)
    revision_to_hash = temp['revision_to_hash']
    
for result in results:
    string = result[0]
    for i in range(len(string)):
        if string[i]!="(":
            continue
        else:
            break
    if i+1!=len(string):
        benchmark = string[:i]
        param = string[i:]
    else:
        benchmark = string
        param = "(default)"
    name = benchmark + "-" + trans[result[2]['Cython']]
    if not name in dict:
        dict[name] = {}
    dict[name][param] = {}
    dict[name][param]['last_v'] = result[4]
    dict[name][param]['best_v'] = result[5]
    # (before, after, value_before, best_value_after)
    dict[name][param]['regression_pos'] = result[6]
    for j in range(len(dict[name][param]['regression_pos'])):
        for i in range(2):
            if dict[name][param]['regression_pos'][j][i] is not None:
                dict[name][param]['regression_pos'][j][i] = revision_to_hash[str(dict[name][param]['regression_pos'][j][i])]
    
with open("./regression.json", "w+") as f:
    json.dump(dict, f, indent=2)
