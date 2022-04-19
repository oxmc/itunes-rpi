import json

input_file = open('media.json').read()
json_array = json.loads(input_file)
json_array = json_array['media']

#print(json_array)

for item in json_array:
    item = "{"+item+"}"
    item = item.replace("'", '"')
    print(item)
    js = json.loads(item['floc'])
    print(js)
    #print(json.dumps(item, indent = 4, sort_keys=True))
    for minfo in js:
        print(minfo)
        print(minfo['floc'])
        print(minfo['title'])
        print(minfo['album'])
