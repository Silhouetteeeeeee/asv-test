import os
import requests
import json
import pandas as pd
import itertools as it
import time
import pandas as pd
import random


requests.packages.urllib3.disable_warnings()
requests.adapters.DEFAULT_RETRIES = 5    
# 11

def f(str):
    return "null" if str == None else str

def product(param):
    size = len(param)
    if size==0: 
        return param
    results = []
    def f(param, size, list = []):
        for p in param[0]:
            list.append(p)
            count = len(list)
            if(count == size):
                results.append(list.copy())
                list.pop()
                continue
            f(param[1:], size, list)
            list.pop()
        
        
    f(param, len(param))
    return results


# def write_to_csv(paths, results):
    
    
def getData(flag = 0):
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
    }

    proxies={
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809'  # https -> http
    }
    url = "https://pv.github.io/numpy-bench/index.json"
    try:
        # 跳过爬取
        if flag:
            raise requests.exceptions.ConnectionError
        
        r = requests.get(url= url, headers=headers, proxies=proxies)
        results = r.json()
    
        revision_to_hash = results['revision_to_hash'] # 获取revison到hash值的转换
        revision_to_date = results['revision_to_date']
        tags = results['tags'] # 获取revision到版本号的转换
        benchmarks = results['benchmarks'] # 获得所有的benchmarks
        graph_param_list = results['graph_param_list']
        benchmarks_list = {}
        
        
        for benchmark in benchmarks:
            name = benchmarks[benchmark]['name']
            params = benchmarks[benchmark]['params']
            params_name = benchmarks[benchmark]['param_names']
            
            benchmarks_list[name] = {}
            benchmarks_list[name]['param_name'] = params_name
            benchmarks_list[name]['params'] = params
        
        to_json = {
            "benchmarks_list":benchmarks_list,
            'graph_param_list':graph_param_list,
            "revision_to_hash": revision_to_hash,
            "revision_to_date": revision_to_date,
            "tags": tags
        }
        with open("./temp.json", "w+") as file:
            json.dump(to_json, file, indent=2, sort_keys=True, ensure_ascii=False)
    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        with open('./temp.json') as fp:
            results = json.load(fp)
            benchmarks_list = results['benchmarks_list']
            graph_param_list = results['graph_param_list']
            revision_to_hash = results['revision_to_hash'] # 获取revison到hash值的转换
            revision_to_date = results['revision_to_date']
            tags = results['tags'] # 获取revision到版本号的转换
        
    return benchmarks_list, graph_param_list, revision_to_hash, revision_to_date, tags

def getGraghData(benchmarks, graph_param_list, revision_to_hash):
    ua_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
           "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
           "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
           ]
    headers = {
    "User-Agent": random.choice(ua_list)
    }

    proxies={
    'http': None,
    'https': 'http://127.0.0.1:10809'  # https -> http
    }
    count = 0
    
    dict = {}
    
    for benchmark in benchmarks:
        bench_param_name = benchmarks[benchmark]['param_name']
        bench_params = benchmarks[benchmark]['params']
        sorted_param = product(bench_params)
        for param in graph_param_list:
            count += 1
            print(count)
            Cython = f(param['Cython'])
            arch = f(param['arch'])
            cpu = f(param['cpu'])
            machine = f(param['machine'])
            num_cpu = f(param['num_cpu'])
            os = f(param['os'])
            python = f(param['python'])
            ram = f(param['ram'])
            setuptools = f(param['setuptools'])
        
            url = "https://pv.github.io/numpy-bench/graphs/Cython-"+ Cython +"/arch-"+ arch +"/branch-main/cpu-"+ cpu +"/machine-" + machine + "/num_cpu-" + num_cpu + "/os-" + os + "/python-" + python + "/ram-" + ram + "/setuptools-" + setuptools + "/six/"+ benchmark +".json?timestamp=1643927988611"
            
            print(param)
            print(benchmark)
            try:
                r = requests.get(url=url, headers=headers, proxies=proxies, verify=False)
                results = r.json()
            except (json.decoder.JSONDecodeError, requests.exceptions.JSONDecodeError):
                continue
            except:
                for i in range(100):
                    r = requests.get(url=url, headers=headers, proxies=proxies, verify=False)
                    if r.status_code == 200:
                        results = r.json()
                        break
            # session = requests.Session()
            # session.trust_env = False
            # r = session.get()
            strs = []
            data = {'hash':[]}
            if not len(sorted_param) == 0:
                for param in sorted_param:
                    str1 = ""
                    for i, name in enumerate(bench_param_name):
                        str1 += name + "-" + param[i].strip("'")
                        if i != len(bench_param_name)-1:
                            str1 += ","
                    strs.append(str1)
                    data[str1] = []
            else:
                strs.append('default')
                data[strs[0]] = []  
            #TODO: 读取数据存到json中
            for result in results:
                id = str(result[0])
                hash = revision_to_hash[id]
                ts = result[1]
                data['hash'].append(hash)
                if type(ts) == list:
                    for i, t in enumerate(ts):
                        data[strs[i]].append(t)
                else:
                    data['default'] = ts
            
            dict[benchmark+"-Param"+str(count%3)] = data
            
            time.sleep(1)
    with open('./benchmarks_list.json', "a+") as fp:
        json.dump(dict, fp, indent=2)

if __name__ == "__main__":
    benchmarks, graph_param_list, revision_to_hash, revision_to_date, tags = getData()
    print(graph_param_list)
    getGraghData(benchmarks, graph_param_list, revision_to_hash)