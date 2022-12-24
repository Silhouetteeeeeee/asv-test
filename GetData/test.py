import json

for i in range(3):
    with open("test.json", "a+") as fp:
        data = i
        json.dump({
            "data" : data
        }, fp)