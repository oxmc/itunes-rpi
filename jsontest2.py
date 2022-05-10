import json
import ast

with open("test.json") as fr:
    with open("test2.json", "w") as fw:
        print(fr)

        for line in fr:
            json_dat = json.dumps(ast.literal_eval(line))
            dict_dat = json.loads(json_dat)
            json.dump(dict_dat, fw)
            fw.write("\n")