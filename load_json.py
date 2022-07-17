import json
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
json_dir = f"{base_dir}\json"

os.chdir(json_dir)
data_from_json = dict()
for fn in os.listdir():
    with open(fn, "r") as file_for_read:
        data = json.load(file_for_read)
        json_string = json.dumps(data)
        data_from_json.update(json.loads(json_string))

# for k,v in data_from_json.items():
#     print(k,v)
#
# print(len(data_from_json))

