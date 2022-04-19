import json

input_file = open('media.json').read()
json_array = json.loads(input_file)
json_array = json_array['media']

#print(json_array)

pairs = json_array[0].items()
for key, value in pairs:
    print(value)

for item in json_array:
    item = "{"+item+"}"
    print(item)
    item = item.replace("'", '"')
    print(item)
    js = json.loads(item)
    print(js)
    for pDetails in js:
        print(pDetails)
        print(pDetails['floc'])
        print(pDetails['title'])
        print(pDetails['album'])
