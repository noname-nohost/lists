import json


with open("main.json", "r") as fp:
    data = json.load(fp)

    keys = list(data.keys())
    keys.sort()
    # print(data)
    for k in keys: print("- [{}](data/{})".format(k, data[k].get("filename", "")))

print(f"Number of data sets {len(keys)}")